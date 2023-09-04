from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login' ),
    path('register/', views.registration, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout, name='logout')

]