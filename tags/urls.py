from django.urls import path
from tags.views import detail_tag

urlpatterns = [
    path('detail-tag/<int:id>/', detail_tag, name='detail_tag'),
]