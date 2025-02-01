from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name='reset/password_reset_form.html'
    ), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='reset/password_reset_done.html'
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='reset/password_reset_confirm.html'
    ),name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/password_reset_complete.html'
    ), name="password_reset_complete"),
    path('', include('django.contrib.auth.urls')),
]
