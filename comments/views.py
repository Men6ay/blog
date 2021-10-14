from django.shortcuts import redirect, render
from comments.models import Comment

def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST.get('text')
        comment.text = text
        comment.save()
        return redirect('index')
    return render(request, 'comments/update.html')

def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    return render(request, 'comments/delete.html')
