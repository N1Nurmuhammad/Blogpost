from dataclasses import fields

# from yaml import serialize
from rest_framework import serializers
from blog.models import *


class BlogsSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model = PagesModel
        # fields = ['title', 'body', 'image', 'username', ]
        # fields = ['title_uz', 'body_uz', 'image_uz', 'title_ru', 'body_ru', 'image_ru', 'title_en', 'body_en', 'image_en', 'username',]
        fields = '__all__'

    # def get_username_from_author(self, obj):
        # return obj.author.phone_number

class CommentsSerilizer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = CommentModel
        fields = '__all__'

    def get_username_from_author(self, comment):
        return comment.author.email


