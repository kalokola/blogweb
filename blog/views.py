from django.shortcuts import render

from blog.models import Post

# Create your views here.

def home_page(request):
    context = dict()
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request,'home-page.html', context)

def about_page(request):
    return render(request,'about.html')

def all_posts(request):
    context = dict()
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'all-posts.html', context)