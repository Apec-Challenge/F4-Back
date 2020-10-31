from .models import Place
from .serializers import PlaceSerializer, PlacePutSerializer, PlaceLikeSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from django.db.models import Count, F
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
    serializer_class = PlacePutSerializer
    lookup_field = 'place_id'


class PlaceTitleFilter(filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'title': ['icontains']
        }


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlacePutSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('place_id', 'title')
    filterset_class = PlaceTitleFilter
    http_method_names = ['get', 'post']

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q == 'review_count':
            return Place.objects.all().order_by('-counts')
        if q == "like_count":
            return Place.objects.annotate(like_count=Count('user_likes')).order_by('-like_count')
