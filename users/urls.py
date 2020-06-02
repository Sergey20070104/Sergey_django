from django.urls import path
from.views import register,ProfileView
from django.contrib.auth import views as authViews

urlpatterns = [
    path('auth/',authViews.LoginView.as_view(
        template_name='users/auth.html'
    ), name='auth'),
    path('reg/',register
    , name='reg'),
    path('exit/',authViews.LogoutView.as_view(
        template_name='users/exit.html'
    ), name='exit'),
    path('profile/',ProfileView.as_view(
        template_name='users/profile.html'
    ), name='profile')
]