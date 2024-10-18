from django.db import models  
from django.contrib.auth.models import User  
  
class Category(models.Model):  
  name = models.CharField(max_length=255)  
  
class Tag(models.Model):  
  name = models.CharField(max_length=255)  
  
class BlogPost(models.Model):  
  title = models.CharField(max_length=255)  
  content = models.TextField()  
  author = models.ForeignKey(User, on_delete=models.CASCADE)  
  category = models.ForeignKey(Category, on_delete=models.CASCADE)  
  tags = models.ManyToManyField(Tag, blank=True)  
  published_date = models.DateTimeField(auto_now_add=True)  
  created_date = models.DateTimeField(auto_now_add=True)
