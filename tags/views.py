from django.shortcuts import render,redirect
from tags.models import Tag

def detail_tag(request,id):
    tag=Tag.objects.get(id=id)
    return render(request,'tags/detail.html',{'tag':tag})

# def update_tag(request,id):
    