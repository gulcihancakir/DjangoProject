from rest_framework.serializers import ModelSerializer
from news.models import News,Category



class NewsLikeSerializer(ModelSerializer):
    class Meta:
        model=News
        fields=[

                'like',
]


class NewsDislikeSerializer(ModelSerializer):
    class Meta:
        model=News
        fields=[

                'dislike',
]



class NewsListSerializer(ModelSerializer):
    class Meta:
        model=News
        fields=[
            'id',
            'title',
            'image',
            'context',
]
class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model=News
        fields=[
            'id',
            'title',
            'context',
]

class NewsCreateSerializer(ModelSerializer):
    class Meta:
        model=News
        fields=[
            'category',
            'title',
            'context',
            'published_date',
]

class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model=News
        fields=[
          
            'title',
            
            'context',
            
            
            ]

