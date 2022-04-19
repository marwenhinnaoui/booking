from urllib import response
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import hotel, rooms

# User Serializer
class RoomsSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField()
    def get_hotel(self, obj):
        return obj.hotel.nameHotel 
        


    class Meta:
        model = rooms
        fields = ('id', 'person', 'image', 'hotel')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], email=validated_data['email'], password=validated_data['password'],is_staff=validated_data['is_staff'] )
        return user
