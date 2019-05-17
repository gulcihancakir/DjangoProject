from django.urls import path

from .views import CommentListAPIView,CommentDetailAPIView

urlpatterns = [
    path('',CommentListAPIView.as_view(), name='list'),
    path('<int:pk>/',CommentDetailAPIView.as_view(), name='detail'),
  
]