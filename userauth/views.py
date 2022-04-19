from imp import is_frozen
from unicodedata import name
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer, RoomsSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from .models import rooms
from rest_framework import status

# Create your views here.


def userauth(request):
    return HttpResponse('userauth')


class RoomList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']
    queryset = rooms.objects.all()
    def get_serializer_class(self):
        return RoomsSerializer
    def ViewAllAPI(self, request):
        queryset = self.get_queryset()

        # 1. List all
        if request.method == 'GET':
            # _rooms = rooms.objects.all()
            roomsSerializer = RoomsSerializer(queryset, many=True)
            return JsonResponse(roomsSerializer.data)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'token': AuthToken.objects.create(user)[1]
    })


class RegisterAPI(generics.GenericAPIView):
    
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data
        })







