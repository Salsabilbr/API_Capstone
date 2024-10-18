from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response  
from rest_framework.views import APIView  
from .models import BlogPost  
from .serializers import BlogPostSerializer  
  
class BlogPostList(APIView):  
  def get(self, request):  
    posts = BlogPost.objects.all()  
    serializer = BlogPostSerializer(posts, many=True)  
    return Response(serializer.data)  
  
  def post(self, request):  
    serializer = BlogPostSerializer(data=request.data)  
    if serializer.is_valid():  
    serializer.save()  
    return Response(serializer.data, status=201)  
    return Response(serializer.errors, status=400)  
  
class BlogPostDetail(APIView):  
  def get(self, request, pk):  
    post = BlogPost.objects.get(pk=pk)  
    serializer = BlogPostSerializer(post)  
    return Response(serializer.data)  
  
  def put(self, request, pk):  
    post = BlogPost.objects.get(pk=pk)  
    serializer = BlogPostSerializer(post, data=request.data)  
    if serializer.is_valid():  
    serializer.save()  
    return Response(serializer.data)  
    return Response(serializer.errors, status=400)  
  
  def delete(self, request, pk):  
    post = BlogPost.objects.get(pk=pk)  
    post.delete()  
    return Response(status=204)
