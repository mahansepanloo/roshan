from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views
app_name = 'auth-token'
urlpatterns = [
    path('token/', auth_views.obtain_auth_token, name='login'),
    path('token/logout/', views.LogoutViwe.as_view(), name='logout'),
    path('register/', views.UserRegistersViwe.as_view(), name='register'),
]