from django.contrib import admin
from django.urls import URLPattern, path
from . import views
from knox import views as knox_views

urlpatterns=[
    path('', views.dashboard, name="dashboard"),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]

