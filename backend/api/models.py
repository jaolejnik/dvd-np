from django.db import models
from rest_framework import serializers


class Comment(models.Model):
    username = models.CharField(max_length=50)
    message = models.TextField()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
