from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect

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


def create_post(request: HttpRequest):
    if not request.user.is_editor: # same as request.user.is_editor == False
        raise Http404
    
    context = dict()

    if request.method == "POST":
        data = request.POST
        print("This is our data: ", data)

        # extract data
        title = data.get("title")
        content = data.get("content")

        if not title: # same as title == "" or title is None
            context['title_required'] = True
            context['title_error'] = "`title` is required"

        else:
            if request.user.is_editor:
                # create your post
                Post.objects.create(
                    title = title, 
                    content = content,
                    user = request.user # by deafult every reqest has a known user
                )

        # return redirect("home-page")

    return render(request, 'create-post.html', context)