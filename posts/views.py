from django.shortcuts import render
from .serializers import PostSerializer
# Create your views here.
from rest_framework import generics,permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly

class PostListApiView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes=(permissions.IsAuthenticated,)



class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes=(permissions.IsAuthenticated,)
    permissions=(permissions.IsAuthenticatedOrReadOnly)