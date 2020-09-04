from django.conf import settings
from rest_framework import serializers
from .models import Feed

MAX_FEED_LENGTH = settings.MAX_FEED_LENGTH
FEED_ACTION_OPTIONS = settings.FEED_ACTION_OPTIONS

class FeedActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip() # "Like " -> "like"
        if not value in FEED_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for POST")
        return value


class FeedCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Feed
        fields = ['id', 'content', 'likes']
    
    def get_likes(self, obj):
        return obj.likes.count()
    
    def validate_content(self, value):
        if len(value) > MAX_FEED_LENGTH:
            raise serializers.ValidationError("This post is too long")
        return value



class FeedSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = FeedCreateSerializer(read_only=True)
    name = serializers.CharField(read_only=True, source="user.name")
    class Meta:
        model = Feed
        fields = ['id', 'name', 'content', 'likes', 'is_share', "parent"]

    def get_likes(self, obj):
        return obj.likes.count()