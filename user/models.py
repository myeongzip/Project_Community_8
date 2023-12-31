from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=200, blank=True, default="Bio")
    image = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='profile_pics')
    following = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="followers")
    
    
    def __str__(self):
        return f'{self.username}'