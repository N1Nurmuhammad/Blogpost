from dataclasses import fields
from rest_framework import serializers
from blog.models import *


class BlogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PagesModel
        # fields = ['title', 'body', 'image', 'author', ]
        fields = '__all__'
