from dataclasses import fields
from django import forms
from .models import *

class PagesForm(forms.ModelForm):

    class Meta:
        model = PagesModel
        fields = ['title_uz', 'body_uz', 'image_uz', 'title_ru', 'body_ru', 'image_ru', 'title_en', 'body_en', 'image_en']


class CommentsForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text']