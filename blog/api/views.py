from blog.models import *
from blog.api.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })



# CUSTOM BLOGS VIEWW    
# @api_view(['GET'])
# def blogs_api_view(request):
#     blogs = PagesModel.objects.all()
#     serializer = BlogsSerializer(blogs, many = True)
#     return Response(serializer.data)

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

@api_view(['PUT', "GET" ])
# @permission_classes((IsAuthenticated,))
def blog_update_api_view(request, pk):

    try:
        blog_post = PagesModel.objects.get(pk=pk)
    except PagesModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have the permission to edit that."})

    if request.method == "GET":
        blogs = get_object_or_404(PagesModel, pk = pk)
        serializer = BlogsSerializer(blogs)
        return Response(serializer.data)

    if request.method == "PUT":
        serializers = BlogsSerializer(blog_post, data=request.data)
        data = {}
        if serializers.is_valid():
            serializers.save()
            data["success"] = "Successfully updated"
            return Response(data=data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiBlogListView(ListAPIView):
    queryset = PagesModel.objects.all()
    serializer_class = BlogsSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # pagination_classes = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ('title', 'body', 'author__username')