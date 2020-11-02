from requests import Response
from django.http import HttpResponse
from .models import Funding, MainFunding,FundingComment
from accounts.models import User
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django_filters import FilterSet, CharFilter
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.viewsets import ModelViewSet
from .serializers import FundingSerializer, FundingPutSerializer, FundingDateSerializer
from django.db.models import Count, F, Q
from .serializers import (
    FundingSerializer,
    FundingPutSerializer,
    MainFundingSerializer,
    FundingCommentSerializer,
    MainFundingPutSerializer,
    FundingCommentPutSerializer,
)
from datetime import datetime


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


class FundingKeywordFilter(FilterSet):
    class Meta:
        model = Funding
        fields = {
            'id': ['exact']
        }




class FundingViewSet(ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    # filterset_class = FundingFilter
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'created_at', 'title', 'description', 'content_text', 'ended_at')
    http_method_names = ['get', 'post']
    filterset_class = FundingKeywordFilter
    lookup_field = 'like_count'

    def get_queryset(self):
        orderbyList = ['created_at']
        q = self.request.GET.get('q')
        end_funding = Funding.objects.order_by('-ended_at').first()
        end_date = end_funding.ended_at
        start_funding = Funding.objects.order_by('ended_at').first()
        start_date = start_funding.ended_at

        if q == 'like_count':
            return Funding.objects.annotate(like_count=Count('user_likes')).order_by('-like_count')
        elif q == "completed":
            return Funding.objects.filter(ended_at__range=[start_date, datetime.now()])
        elif q == "deadline":
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


def FundingLike(request, user, id):
    if request.method == 'GET':
        print(user, id)
        place = Funding.objects.get(id=id)
        print(place.user_likes.all().values('nickname'))
        user_id = User.objects.get(nickname=user)
        print(user_id)
        if place.user_likes.filter(nickname=user).exists():
            place.user_likes.remove(user_id)
            print("좋아요 취소")
        else:
            place.user_likes.add(user_id)
            print("좋아요")
    return HttpResponse(status=200)


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
