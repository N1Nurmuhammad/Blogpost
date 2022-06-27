from django.urls import path, include
from blog.api.views import *

urlpatterns = [
    path('blogs', blogs_api_view , name='blogs' ),
    path('create', create_blog_api, name='create'),
    path('detail/<int:pk>', blog_detail_api_view, name='detail'),
    path('comments/<int:pk>', comments_blog_view, name='comments'),
    path('delete/<int:pk>', blog_delete_api_view, name='delete'),

]
