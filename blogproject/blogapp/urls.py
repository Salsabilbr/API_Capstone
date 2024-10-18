from django.urls import path  
from . import views  
  
urlpatterns = [  
  path('posts/', views.BBlogPostDetail.as_view()),  
  path('users/', views.UserViewSet.as_view()),  
  path('categories/', views.CategoryViewSet.as_view()),  
  path('tags/', views.TagViewSet.as_view()),  
]
