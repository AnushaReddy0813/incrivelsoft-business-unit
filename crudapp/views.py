from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import TimeStampModel,Business
from .serializers import TimeStampModelSerializer,BusinessSerializer
# Create your views here.
class BusinessCreateApi(generics.CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
class BusinessGetApi(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
class BusinessUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
class BusinessDeleteApi(generics.DestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer