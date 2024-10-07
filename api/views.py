from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import CitySerializer, City


# Create your views here.

class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
