from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create views

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/car-list/',
        'Filter by model': '?model=',
        'Filter by price': '?price=',
    }

    return Response(api_urls)

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model', 'price']


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all
    serializer_class = CarSerializer


