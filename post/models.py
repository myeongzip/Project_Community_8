from django.db import models
from community import settings

from user.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey("user.User", on_delete = models.CASCADE, related_name="post")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(blank=True, null=True, upload_to='post_pics', default='default.jpg')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    
    def __str__(self):
        return self.title


class Comment(models.Model):   
    user = models.ForeignKey("user.User", on_delete = models.CASCADE, related_name="comments")   
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.content
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
