from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('send_request/<str:username>/', views.send_friend_request, name='send-request'),
    path('accept_request/<int:pk>/<str:from_user>', views.accept_friend_request, name='accept_request'),
    path('delete_request/<int:pk>/', views.delete_friend_request, name='delete-request'),
    path('unfriend/<int:pk>/', views.unfriend, name='unfriend'),
    path('friend_requests/', views.friends_request, name='friend-requests'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<str:username>/', views.ProfileUpdateView.as_view(), name='profile-edit'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='reset/password_reset_form.html'
    ), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='reset/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
]
