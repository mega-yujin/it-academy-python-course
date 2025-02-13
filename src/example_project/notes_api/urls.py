from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tags', views.TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]