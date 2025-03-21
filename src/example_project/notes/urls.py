from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.HomeView.as_view(), name='index'),
    # path('add_note', views.add_note, name='add_note'),
    path('add_note', views.AddNoteView.as_view(), name='note_create'),
    path('favorites', views.FavoritesView.as_view(), name='favorites'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/toggle-favorite/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('note/<int:note_pk>/file/<int:pk>/delete/', views.delete_note_file, name='delete_note_file'),
    path('note/<int:pk>/share', views.ShareNoteView.as_view(), name='share_note')
]
