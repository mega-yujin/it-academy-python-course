from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_note', views.add_note, name='add_note'),
]
