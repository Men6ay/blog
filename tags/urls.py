from django.urls import path
from tags.views import delete_tag, detail_tag, update_tag

urlpatterns = [
    path('<int:id>/', detail_tag, name='detail_tag'),
    path('update-tag/<int:id>/', update_tag, name='update_tag'),
    path('delete-tag/<int:id>/', delete_tag, name='delete_tag'),
]