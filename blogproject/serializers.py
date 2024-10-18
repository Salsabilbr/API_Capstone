# api/serializers.py  
from rest_framework import serializers  
from .models import BlogPost  
  
class BlogPostSerializer(serializers.ModelSerializer):  
   class Meta:  
      model = BlogPost  
      fields = ['title', 'content', 'author', 'category', 'tags']  
  
   def validate_title(self, value):  
      if not value:  
        raise serializers.ValidationError('Title is required')  
      return value  
  
   def validate_content(self, value):  
      if not value:  
        raise serializers.ValidationError('Content is required')  
      return value

