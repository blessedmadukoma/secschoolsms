from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register, name='register'),
  path('staff_register/', views.staff_register, name='staff_register'),
  path('staff_login/', views.staff_login, name='staff_login'),
  path('login/', views.loginUser, name='login'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('logout/', views.logoutUser, name='logout'),
]