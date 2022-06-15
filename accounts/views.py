
from django.http import HttpResponse
from accounts.forms import *
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView


class home_view(TemplateView):
    template_name = 'base.html'

def registration_view(request):
    context={}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('blog:blogs')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, "signup.html", context)



def account_authentication(request):
    context={}
    user = request.user
    if user.is_authenticated:
        return redirect('blog:blogs')


    if request.POST:
        form = AccountAuthentificationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('blog:blogs')

    else:
        form = AccountAuthentificationForm()
    context['login_form'] = form 
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('blog:blogs')



def edit_account_view(request, pk):
    context = {}

    user = request.user
    # print(user)
    if not user.is_authenticated:
        return redirect('accounts:login')

    blog_post = get_object_or_404(Account, pk=pk)
    # print(blog_post.email)

    if str(blog_post.email) != str(user):
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateAccountForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect("blog:blogs")
    form = UpdateAccountForm(
        initial={
            'f_name':blog_post.f_name,
            'l_name': blog_post.l_name,
            'sex': blog_post.sex,
            'date_birthday':blog_post.date_birthday,
        }
    )

    context['form'] = form
    return render(request, 'update_account.html', context)