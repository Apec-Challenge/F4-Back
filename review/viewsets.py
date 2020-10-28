from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters import FilterSet
from .models import Review
from .serializers import ReviewListSerializer, ReviewUpdateSerializer, ReviewDeleteSerializer
from rest_framework.generics import (
    UpdateAPIView, DestroyAPIView,
)


# class ReviewFilter(FilterSet):
#     class Meta:
#         model = Review
#         fields = {
#             # 'title': ['icontains'],
#             'created_at': ['date', 'date__lte', 'date__gte'],
#             'user': ['exact'],
#         }


class ReviewListViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('created_at')
    serializer_class = ReviewListSerializer
    # filterset_class = ReviewFilter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user','place')
    http_method_names = ['get', 'post']


class ReviewUpdateViewSet(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    lookup_field = 'id'


class ReviewDeleteViewSet(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDeleteSerializer
    lookup_field = 'id'





