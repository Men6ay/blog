from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=155)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    creat_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return f'{self.title}======={self.creat_at}'
