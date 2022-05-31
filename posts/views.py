from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return render(request, "home.html")

def posts(request):
    posts = Post.objects.all() # SELECT * FROM posts
    
    # print(posts)
    # return HttpResponse("Posts")

    return render(request, "posts.html", context={
        "posts": posts
    })

def recent_posts(request):
    # ASC => Without -
    # DESC => With - like ".order_by(-created_date)"
    # recent_posts = Post.objects.all().order_by("created_date") # SELECT * FROM posts ORDER BY created_date [ASC]
    recent_posts = Post.objects.all().order_by("-created_date") # SELECT * FROM posts ORDER BY created_date DESC

    return render(request, "recent-posts.html", {
        "recent_posts": recent_posts
    })

def post(request, id):
    post = Post.objects.get(id=id)

    return render(request, "post.html", {"post": post})