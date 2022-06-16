from urllib import response
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import hotel, reservation, rooms

# User Serializer
class RoomsSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField()
    def get_hotel(self, obj):
        return {"nameHotel": obj.hotel.nameHotel, "location":obj.hotel.location,"description":obj.hotel.description, "stars":obj.hotel.stars,}

    class Meta:
        model = rooms
        fields = ('id', 'person', 'image', 'hotel')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')

        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = ('id', 'client', 'room','person', 'dateStart', 'dateEnd')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], email=validated_data['email'], password=validated_data['password'],is_staff=validated_data['is_staff'] )
        return user
