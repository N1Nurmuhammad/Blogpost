import email
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import *
from .forms import *
from accounts.models import Account


class Vieww(TemplateView):
    template_name = 'body.html'


# def topblogs(request):
#     blogs = 

def page_create(request):
    if request.method == "POST":
        instance = PagesForm(request.POST or None, request.FILES or None)
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')

        if instance.is_valid():
            obj = instance.save(commit=False)
            author = Account.objects.filter(email=user.email).first()
            try:
                author = Account.objects.get(email=user.email)
            except:
                return Account.DoesNotExist
            obj.author = author
            obj.save()
        # messages.success(request, f'Ссылка добавлена')
    else:
        instance = PagesForm()
    
    return render(request, 'create.html', {'form': instance})