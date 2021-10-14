from django import urls
from django.urls import path
from comments.views import update_comment,delete_comment

urlpatterns = [
    path('update_comment/<int:id>/', update_comment,name='update_comment'),
    path('delete_comment/<int:id>/', delete_comment,name='delete_comment'),
]