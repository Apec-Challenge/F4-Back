from rest_framework import viewsets, request
from django_filters import rest_framework as filters
from .models import Review
from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewListSerializer, ReviewUpdateSerializer, ReviewDeleteSerializer
from rest_framework.generics import (
    UpdateAPIView, DestroyAPIView,
)
from django.db.models import Count, F



# class ReviewFilter(FilterSet):
#     class Meta:
#         model = Review
#         fields = {
#             # 'title': ['icontains'],
#             'created_at': ['date', 'date__lte', 'date__gte'],
#             'user': ['exact'],
#         }


class ReviewUpdateViewSet(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    lookup_field = 'id'


class ReviewDeleteViewSet(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDeleteSerializer
    lookup_field = 'id'


class ReviewListViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    # filterset_class = ReviewFilter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user', 'place')
    http_method_names = ['get', 'post']

    def get_queryset(self):
        orderbyList = ['-created_at']
        q = self.request.GET.get('q')

        if q == "like_count":
            return Review.objects.annotate(like_count=Count('user_likes')).order_by('-like_count')
        else:
            return Review.objects.all().order_by(*orderbyList)

