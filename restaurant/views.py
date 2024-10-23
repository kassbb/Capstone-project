from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import permissions
# Vue pour la page d'accueil
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):

    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 