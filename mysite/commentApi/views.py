from django.shortcuts import render
from news.models import Comment,News,Category
from django.shortcuts import render, get_object_or_404
# Create your views here.

from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import NewsSerializerList, NewsDetailSerializer


class CommentListAPIView(ListAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializerList

class CommentDetailAPIView(RetrieveAPIView):
    queryset=News.objects.all()
    serializer_class=NewsDetailSerializer



