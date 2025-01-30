from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.HomeView.as_view(), name='index'),
    # path('add_note', views.add_note, name='add_note'),
    path('add_note', views.AddNoteView.as_view(), name='add_note'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
]
