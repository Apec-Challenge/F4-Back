from .models import Place, PPE, GooglePlace
from .serializers import PlaceSerializer
from rest_framework.viewsets import ModelViewSet
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    http_method_names = ['get', 'post']

class PlaceCreateAPIView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    http_method_names = ['post']

class PlaceUpdateAPIView(UpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'google_api'

class PlaceDeleteAPIView(DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'google_api'