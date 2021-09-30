from django.shortcuts import render,redirect
from posts.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        post_obj = Post.objects.create(title = title, text = text)
        return redirect('index')
    return render(request, 'posts/create.html')
