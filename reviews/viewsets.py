from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters import FilterSet
from .models import Review
from .serializers import ReviewListSerializer, ReviewCreateSerializer, ReviewUpdateSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
)


class ReviewListViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('created_at')
    serializer_class = ReviewListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)
    http_method_names = ['get']


class ReviewCreateViewSet(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    http_method_names = ['post']


class ReviewUpdateViewSet(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    lookup_field = 'id'


# class ReviewDeleteViewSet(DestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewDeleteSerializer
#     lookup_field = 'id'
