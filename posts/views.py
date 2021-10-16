from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect
from posts.models import Post,Like
from tags.models import Tag
from comments.models import Comment
from django.db.models import Q

def index(request):
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = Post.objects.filter(Q(title__icontains=key) | Q(user__username__icontains=key))
    else:
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
                comment_obj = Comment.objects.create(user=request.user, post=posts, text=text)
                return redirect('detail', posts.id)
            except:
                print('Error')
        if 'comments_comment' in request.POST:
            id = int(request.POST.get('comments_comment'))
            print(id)
            comment_obj = Comment.objects.get(id=id)
            try:
                text = request.POST.get('text')
                comment_create = Comment.objects.create(user=request.user, post=posts,text=text,parent=comment_obj)
                return redirect('detail', posts.id)
            except:
                print('ERROR')
        if 'like' in request.POST:
            try:
                like = Like.objects.get(user=request.user,post = posts)
                like.delete()
            except:
                Like.objects.create(user = request.user, post=posts)
    return render(request, 'posts/detail.html', {"posts":posts})