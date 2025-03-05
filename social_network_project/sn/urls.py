from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListViewRecent.as_view(), name='post-list-recent'),
    path('posts/<str:username>/', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/like/', views.like_post, name='like-post'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('comment/<int:post_id>/add/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]