import django


from django.urls import path, include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blogs'),
    path('create', page_create, name='create'),
    path('detail/<int:pk>', detail_blog_view, name='detail'),
    path('update/<int:pk>', edit_blog_view, name="update")

    
]

 