from .models import Place
from .serializers import PlaceSerializer, PlacePutSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
import requests
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)


# 사용자 입력 Place Model ViewSet
class PlaceCreateAPIView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacePutSerializer
    http_method_names = ['post']


class PlaceUpdateAPIView(UpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacePutSerializer
    lookup_field = 'place_id'


class PlaceDeleteAPIView(DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'place_id'


class PlaceTitleFilter(filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'title': ['icontains']
        }


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('place_id', 'title')
    filterset_class = PlaceTitleFilter
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Place.objects.all().order_by('-counts')
