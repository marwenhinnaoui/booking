from django.contrib import admin
from django.urls import URLPattern, path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
router = DefaultRouter()
router.register('post', views.PostReserve, basename='Products')
urlpatterns=[
    path('', views.userauth, name="auth"),
    path('auth/register/', views.RegisterAPI.as_view(), name='register'),
    path('auth/login/', views.LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('all/', views.RoomList.as_view(), name='all'),
    path('', include(router.urls)),
    path ('reservation/', views.ReservationViewSet.as_view()),
    path ('reservation/<int:pk>', views.ReservationViewSet.as_view())
]