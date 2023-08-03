from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models, serializers
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [IsAuthenticated] 


class SingleMenuItemView(RetrieveAPIView, DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated] 

class BookingViewSet(ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated] 

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = serializers.UserSerializer
   permission_classes = [IsAuthenticated] 