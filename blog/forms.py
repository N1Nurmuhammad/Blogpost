from dataclasses import fields
from django import forms
from .models import *

class PagesForm(forms.ModelForm):

    class Meta:
        model = PagesModel
        fields = ['title', 'body', 'image']
        