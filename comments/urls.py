from django import urls
from django.urls import path
from comments.views import comment_index

urlpatterns = [
    path('<int:id>/', comment_index, name = 'comment_index')
]