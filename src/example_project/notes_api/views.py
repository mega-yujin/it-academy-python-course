from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.pagination import PageNumberPagination
from notes.models import Tag, Note, NoteFile
from .serializers import TagSerializer, NoteSerializer, NoteCreateSerializer


class NotesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 10


class NotesRateThrottle(UserRateThrottle):
    rate = '100/minute'


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoteViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    throttle_classes = [NotesRateThrottle]
    pagination_class = NotesPagination

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return NoteCreateSerializer
        return NoteSerializer

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def favorites(self, request):
        favorite_notes = self.get_queryset().filter(is_favorite=True)
        serializer = self.get_serializer(favorite_notes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_fav(self, request, pk):
        note = self.get_object()
        note.is_favorite = not note.is_favorite
        note.save()
        return Response(
            {
                'status': 'success',
                'is_favorite': note.is_favorite,
            }
        )
