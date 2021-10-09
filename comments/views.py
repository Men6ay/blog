from django.shortcuts import render
from posts.models import Post
from comments.models import Comment

def comment_index(request,id):
    post_obj = Post.objects.get(id=id)
    comments = post_obj.comment.all()
    return render(request, 'comments/index.html', {'comments':comments})


