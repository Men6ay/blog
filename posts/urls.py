from django.urls import path
from posts.views import index,create

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name = 'create'),
]