from django.urls import path

from .views import(
    NewsUpdateAPIView,
    NewsListAPIView,
    NewsDetailAPIView,
    NewsDeleteAPIView,
    NewsCreateAPIView,
    NewsLikeAPIView,
    NewsDislikeAPIView,
   

)



urlpatterns = [
    path('',NewsListAPIView.as_view(), name='list'),
    path('new/', NewsCreateAPIView.as_view(), name='api_new'),
    path('<int:pk>/detail', NewsDetailAPIView.as_view(), name='api_detail'),
   
    path('<int:pk>/delete/', NewsDeleteAPIView.as_view(), name='api_delete'),
    path('<int:pk>/edit/',NewsUpdateAPIView.as_view(), name='api_edit'),
    path('<int:pk>/dislike',  NewsDislikeAPIView.as_view(),  name='api_dislike'),
    path('<int:pk>/like',  NewsLikeAPIView.as_view(),  name='api_like'),
]