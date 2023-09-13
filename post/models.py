from django.db import models
from community import settings

from user.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(blank=True, null=True, upload_to='post_pics')
    # likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    
    def __str__(self):
        return self.title
<<<<<<< HEAD
=======

>>>>>>> 926a635289a811d5d5e8d55740c53b193b89c6e8
    
    # @property
    # def view_count(self):
    #     return PostLikes.objects.filter(post=self).count()

class Comment(models.Model):   
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)   
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# class PostLikes(models.Model):
#     user = models.ForeignKey(User)
#     post = models.ForeignKey(Post)
#     created = models.DateTimeField(auto_now_add=True)
 