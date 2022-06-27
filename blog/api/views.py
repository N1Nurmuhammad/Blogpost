from blog.models import *
from blog.api.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404




@api_view(['GET'])
def blogs_api_view(request):
    blogs = PagesModel.objects.all()
    serializer = BlogsSerializer(blogs, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog_api(request):
    serializer = BlogsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def blog_detail_api_view(request, pk):
    blogs = get_object_or_404(PagesModel, pk = pk)
    serializer = BlogsSerializer(blogs)
  
    return Response(serializer.data)


@api_view(['DELETE','GET'])
def blog_delete_api_view(request, pk):
    blogs = get_object_or_404(PagesModel, pk = pk)
    serializer = BlogsSerializer(blogs)
    blogs.delete()
    return Response(serializer.data)

@api_view(['POST','GET'])
def comments_blog_view(request, pk):
    comments = CommentModel.objects.filter(blog_id=pk)
    serializer = CommentsSerilizer(comments, many = True)
    return Response(serializer.data)


