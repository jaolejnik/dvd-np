from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Comment, CommentSerializer


class VueTemplateView(TemplateView):
    template_name = "index.html"
    lookup_field = "id"


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
