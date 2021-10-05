from django.shortcuts import render,redirect
from posts.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        file = request.FILES.get('file')
        post_obj = Post.objects.create(title = title, text = text,image=file)
        return redirect('index')    
    return render(request, 'posts/create.html')

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        file = request.FILES.get('file')
        post_update = Post.objects.get(id=id)
        post_update.title = title
        post_update.text = text
        post_update.image = file
        post_update.save()
        return redirect('index')
    return render(request, 'posts/update.html')

def delete(request, id):
    if request.method == 'POST':
        post_object = Post.objects.get(id = id)
        post_object.delete()
        return redirect('index')
    return render(request, 'posts/delete.html')

def detail(request,id):
    posts = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {"posts":posts})