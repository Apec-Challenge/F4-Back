from .models import Funding
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import FundingSerializer, FundingPutSerializer, FundingDateSerializer



class FundingCreateViewSet(ListCreateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    http_method_names = ['post']


class FundingUpdateAPIView(UpdateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingPutSerializer
    lookup_field = 'id'


class FundingDeleteAPIView(DestroyAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    lookup_field = 'id'


# class FundingFilter(FilterSet):
#     class Meta:
#         model = Funding
#         fields = {
#             'title': ['icontains'],
#             'created_at': ['date', 'date__lte', 'date__gte'],
#             'user': ['exact'],
#         }


class FundingViewSet(ModelViewSet):
    queryset = Funding.objects.all().order_by('created_at')
    serializer_class = FundingSerializer
    # filterset_class = FundingFilter
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']