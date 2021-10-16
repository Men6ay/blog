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

    def get_parent(self):
        return self.comment_post.filter(parent__isnull=True)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_user')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='like_post')

    def __str__(self):
        return self.user.username