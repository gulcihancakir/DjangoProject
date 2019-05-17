from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from news.models import Comment,News,Category

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('name','text') 

class NewsSerializerList(serializers.ModelSerializer):

    comments = CommentSerializer(source='comment_set',many=True)
    class Meta:
         model = News
         fields = ('id','title','image','context','comments')

class NewsDetailSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(source='comment_set',many=True)
    class Meta:
         model = News
         fields = ('id','title','image','context','comments')

"""class NewsSerializerList(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(source='comment_set',many=True)

    class Meta:
        model = News
        fields =  ('id','title','context','comments')  """       