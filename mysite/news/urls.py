from django.urls import path
from . import views

urlpatterns = [

  path('', views.news_list, name='news_list'),
  path('news/<int:pk>/detail', views.news_detail, name='news_detail'),
  path('news/new/', views.news_new, name='news_new'),
  path('news/<int:pk>/delete', views.news_delete, name='news_delete'),
  path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
  path('news/<int:pk>/dislike',  views.news_dislike,  name='news_dislike'),
  path('news/<int:pk>/like',  views.news_like,  name='news_like'),
  path('category/',views.category_list, name='category_list'),
  path('category/<int:pk>/detail', views.category_detail, name='category_detail'),
  path('category/new/', views.category_new, name='category_new'),
  path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
  path('category/<int:pk>/delete', views.category_delete, name='category_delete'),
  


]