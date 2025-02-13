from rest_framework import viewsets
from notes.models import Tag, Note, NoteFile
from .serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
