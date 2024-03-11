from rest_framework import serializers
from .models import BlogPost,StudentPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id","title","content","published_date"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPost
        fields = ["id","Name","Details","published_date"]