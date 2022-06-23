from django.urls import path, include
from blog.api.views import *

urlpatterns = [
    path('blogs', blogs_api_view , name='blogs' ),
    path('create', create_blog_api, name='create'),
    path('detail/<int:pk>', blogs_api_view, name='detail'),

]
