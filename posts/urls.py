from django.urls import path
from posts.views import index,create,update,delete,detail

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name = 'create'),
    path('update/<int:id>/', update, name = 'update'),
    path('delete/<int:id>', delete,name = 'delete'),
    path('detail/<int:id>', detail, name='detail'),
]