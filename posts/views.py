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

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        post_update = Post.objects.get(id=id)
        post_update.title = title
        post_update.text = text
        post_update.save()
        return redirect('index')
    return render(request, 'posts/update.html')

def delete(request, id):
    if request.method == 'POST':
        post_object = Post.objects.get(id = id)
        post_object.delete()
        return redirect('index')
    return render(request, 'posts/delete.html')
