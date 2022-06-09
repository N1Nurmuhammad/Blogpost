from django.shortcuts import render
from django.views.generic import TemplateView


class Vieww(TemplateView):
    template_name = 'base.html'
    