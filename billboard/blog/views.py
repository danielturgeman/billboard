from django.shortcuts import render
from django.utils import timezone
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

    #when hitting the form submit button it automatically refreshes the page on
    #url of post/blog/ which sends a POST request, so lets check if form is valid
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
        return render(request, 'posts.html', {"posts": post_list})


    # for get request
    else:
        form = PostForm()
        return render(request, 'form.html', {'posts': post_list, 'form': form})

