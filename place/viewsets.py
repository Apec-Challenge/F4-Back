from .models import Place
from .serializers import PlaceSerializer
from rest_framework.viewsets import ModelViewSet
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)


# 사용자 입력 Place Model ViewSet
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
    lookup_field = 'place_id'


class PlaceDeleteAPIView(DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'place_id'


