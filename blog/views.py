import email
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import *
from .forms import *
from accounts.models import Account
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404



# class Vieww(TemplateView):
#     template_name = 'body.html'


# def topblogs(request):
#     blogs = 

def page_create(request):
    print('aaa')
    if request.method == "POST":
        print('aa1111111a')

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
            return redirect("blog:blogs")

        # messages.success(request, f'Ссылка добавлена')
    else:
        print('else')
        instance = PagesForm()
    
    return render(request, 'create.html', {'form': instance})



def blog_view(request):
    blog = PagesModel.objects.all()
    
    context = {
        'blog_list':blog,

    }
    return render(request, 'body.html' , context )


def detail_blog_view(request, pk):
    context = {}
    blog_post = get_object_or_404(PagesModel, pk = pk)
    user = request.user
    comments = CommentModel.objects.filter(blog_id = pk)
    context['blog_post'] = blog_post
    context['comments'] = comments
    if request.method == "POST":
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog_post
            new_comment.author = user
            new_comment.save()
            return redirect(f'{request.path}')
    else:
        comment_form = CommentsForm()
    context['comment_form'] = comment_form
    return render(request, 'detail.html', context)



def edit_blog_view(request, pk):
    context = {}
    # print(request.path.split('/')[-1])

    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:login')

    blog_post = get_object_or_404(PagesModel, pk=pk)

    if blog_post.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = PagesForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect("blog:blogs")
    form = PagesForm(
        initial={
            'title':blog_post.title,
            'body': blog_post.body,
            'image': blog_post.image,
            'author':blog_post.author,
        }
    )

    context['form'] = form
    return render(request, 'update.html', context)
# https://stackoverflow.com/questions/67719944/modelform-instance-vs-initial


# def delete_view(request, pk):
#     context= []
#     try:
#         author = Account.objects.get(email=user.email)
#     except:
#         return Account.DoesNotExist