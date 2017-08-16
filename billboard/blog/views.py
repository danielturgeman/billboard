from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Post
from .forms import PostForm


def index(request):
    #List of all post objects
    post_list = Post.objects.order_by('-date')
    for post in post_list:
        print(str(post))

    #posts is the key which contains a list of post objects
    return render(request, 'posts.html', {"posts": post_list})

def post_new(request):
    post_list = Post.objects.order_by('-date')
    form = PostForm()
    return render(request, 'form.html', {'posts': post_list, 'form': form})

