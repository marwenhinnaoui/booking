from django.contrib import admin
from django.urls import URLPattern, path
from . import views
from knox import views as knox_views

urlpatterns=[
    path('', views.userauth, name="auth"),
    path('auth/register/', views.RegisterAPI.as_view(), name='register'),
    path('auth/login/', views.LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('all/', views.RoomList.as_view(), name='all'),
    path('reservation/', views.Reservation.as_view(), name='all'),
]