from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'sub_content', 'image', 'author', 'category', 'tags', 'published_date',
                  'status', 'read_min', 'views_count', 'is_popular']
