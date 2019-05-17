
from rest_framework.generics import ListAPIView,\
    RetrieveAPIView,\
    RetrieveUpdateAPIView,\
    UpdateAPIView,\
    DestroyAPIView,\
    CreateAPIView,\
    RetrieveUpdateDestroyAPIView

    
from rest_framework.response import Response
from rest_framework.request import Request
from news.models import News,Comment
from .serializers import NewsListSerializer,NewsDetailSerializer,NewsLikeSerializer,NewsUpdateSerializer,NewsCreateSerializer, NewsDislikeSerializer
from rest_framework import status


class NewsListAPIView(ListAPIView):
    queryset=News.objects.all()
    serializer_class=NewsListSerializer

    def post(self, request, format=None):


        return Response("ok")

class NewsDetailAPIView(RetrieveAPIView):
    queryset=News.objects.all()
    serializer_class=NewsDetailSerializer
    

class NewsUpdateAPIView(RetrieveUpdateAPIView):
    queryset=News.objects.all()
    serializer_class= NewsUpdateSerializer
    def post(self, request):
     
        return Response("ok")

class NewsCreateAPIView(CreateAPIView):
    queryset=News.objects.all()
    serializer_class= NewsCreateSerializer
  



class NewsDeleteAPIView(DestroyAPIView):
    queryset=News.objects.all()
    serializer_class=NewsDetailSerializer
    def post(self, request, format=None):
        print(request._request.body)
        return Response("ok")

class NewsLikeAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsLikeSerializer

class NewsDislikeAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDislikeSerializer








