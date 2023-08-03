from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from . import models

class MenuSerializer(ModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"