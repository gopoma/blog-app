from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return render(request, "home.html")

def posts(request):
    posts = Post.objects.all() # SELECT * FROM posts
    
    # print(posts)
    # return HttpResponse("Posts")

    return render(request, "posts/posts.html", context={
        "posts": posts
    })

def recent_posts(request):
    # ASC => Without -
    # DESC => With - like ".order_by(-created_date)"
    # recent_posts = Post.objects.all().order_by("created_date") # SELECT * FROM posts ORDER BY created_date [ASC]
    recent_posts = Post.objects.all().order_by("-created_date") # SELECT * FROM posts ORDER BY created_date DESC

    return render(request, "posts/recent-posts.html", {
        "recent_posts": recent_posts
    })

def post(request, id):
    post = Post.objects.get(id=id)

    return render(request, "posts/post.html", {"post": post})

def create_post(request):
    if request.method == "POST":
        post = Post(
            title=request.POST["title"],
            description=request.POST["description"],
            img=request.POST["img"],
            content=request.POST["content"]
        )

        post.save()
        return redirect("/posts")

    return render(request, "posts/create.html")