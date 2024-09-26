from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

