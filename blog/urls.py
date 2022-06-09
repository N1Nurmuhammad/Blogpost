import django


from django.urls import path, include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', Vieww.as_view(), name='blogs')
]

 