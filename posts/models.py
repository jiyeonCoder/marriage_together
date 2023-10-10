from django.db import models
from users.models import User
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_count = models.ManyToManyField(User, related_name='like_posts')

    def __str__(self):
        return str(self.title)
    

class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='작성자')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='포스트', related_name='post_comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)
