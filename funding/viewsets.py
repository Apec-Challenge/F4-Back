from .models import Funding, MainFunding, FundingComment
from rest_framework.generics import (
    UpdateAPIView,
    DestroyAPIView
)
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count, F, Q
from .serializers import (
    FundingSerializer,
    FundingPutSerializer,
    MainFundingSerializer,
    FundingCommentSerializer,
    MainFundingPutSerializer,
    FundingCommentPutSerializer,
    FundingCreateSerializer
)
from datetime import datetime


class FundingCreateViewSet(ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingCreateSerializer
    http_method_names = ['get', 'post']


class FundingUpdateAPIView(UpdateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingPutSerializer
    lookup_field = 'id'


class FundingDeleteAPIView(DestroyAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    lookup_field = 'id'


class FundingKeywordFilter(FilterSet):
    class Meta:
        model = Funding
        fields = {
            'id': ['exact']
        }


class FundingViewSet(ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'created_at', 'title', 'description', 'content_text', 'ended_at')
    http_method_names = ['get', 'post']
    filterset_class = FundingKeywordFilter
    lookup_field = 'like_count'

    def get_queryset(self):
        orderbyList = ['created_at']
        q = self.request.GET.get('q')
        key = self.request.GET.get('key','')

        if q == 'like_count':
            return Funding.objects.annotate(like_count=Count('user_likes')).order_by('-like_count')
        elif q == "completed":
            start_funding = Funding.objects.order_by('ended_at').first()
            start_date = start_funding.ended_at
            return Funding.objects.filter(ended_at__range=[start_date, datetime.now()])
        elif q == "deadline":
            end_funding = Funding.objects.order_by('-ended_at').first()
            end_date = end_funding.ended_at
            return Funding.objects.filter(ended_at__range=[datetime.now(), end_date])
        elif q == "hot":
            return Funding.objects.annotate(user_count=Count('backed_list'))\
                .order_by('-user_count')
        elif q == "achievement":
            return Funding.objects.annotate(achievement_rate=F('funding_amount')/F('funding_goal_amount')) \
                .order_by('-achievement_rate')
        elif q == "keyword":
            search = (Funding.objects.order_by('created_at').filter(Q (title__icontains=key) | Q (content_text__icontains=key) | Q (description__icontains=key)))
            return search
        else:
            return Funding.objects.all().order_by(*orderbyList)


class MainFundingViewSet(ModelViewSet):
    queryset = MainFunding.objects.all()
    serializer_class = MainFundingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'main_funding')
    http_method_names = ['get', 'post']


class MainFundingUpdateAPIView(UpdateAPIView):
    queryset = MainFunding.objects.all()
    serializer_class = MainFundingPutSerializer
    lookup_field = 'id'


class MainFundingDeleteAPIView(DestroyAPIView):
    queryset = MainFunding.objects.all()
    serializer_class = MainFundingSerializer
    lookup_field = 'id'


class FundingCommentViewSet(ModelViewSet):
    queryset = FundingComment.objects.all()
    serializer_class = FundingCommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'content')
    http_method_names = ['get', 'post']


class FundingCommentUpdateAPIView(UpdateAPIView):
    queryset = FundingComment.objects.all()
    serializer_class = FundingCommentPutSerializer
    lookup_field = 'id'


class FundingCommentDeleteAPIView(DestroyAPIView):
    queryset = FundingComment.objects.all()
    serializer_class = FundingCommentSerializer
    lookup_field = 'id'
