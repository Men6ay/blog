from django.shortcuts import render,redirect
from posts.models import Post
from tags.models import Tag
from comments.models import Comment

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        file = request.FILES.get('file')
        tags = request.POST.get('tags')
        post_obj = Post.objects.create(user=request.user,title = title, text = text,image=file)
        if len(tags) != 0:
            try:
                tags_get = Tag.objects.get(title = tags)
                tags_get.posts.add(post_obj)
            except:
                tags_get = Tag.objects.create(title=tags)
                tags_get.posts.add(post_obj)
        return redirect('index')    
    return render(request, 'posts/create.html')

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        file = request.FILES.get('file')
        tags = request.POST.get('tag')
        post_update = Post.objects.get(id=id)
        post_update.title = title
        post_update.text = text
        post_update.image = file
        post_update.save()
        if len(tags) != 0:
            try:
                tags_get = Tag.objects.get(title = tags)
                tags_get.posts.add(post_update)
            except:
                tags_obj = Tag.objects.create(title=tags)
                tags_obj.posts.add(post_update)
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
    if request.method == 'POST':
        if 'comment' in request.POST:
            try:
                text = request.POST.get('text')
                comment_obj = Comment.objects.create(user=request.user, post =posts, text=text)
                return redirect('index')
            except:
                print('Error')
    return render(request, 'posts/detail.html', {"posts":posts})