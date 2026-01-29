from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)


class Articles(models.Model):
    source = models.CharField(max_length=100, null = True, blank=True)
    author = models.CharField(max_length=100, null = True, blank=True)
    title = models.CharField(max_length=100, null = True, blank=True)
    description = models.TextField( null = True, blank=True)
    urls = models.CharField(max_length=100, null = True, blank=True)
    urlToImage = models.CharField(max_length=1000, null = True, blank=True)
    publishedAt = models.CharField(max_length=100, null = True, blank=True)
    content = models.TextField(null = True, blank=True)
    
    def __str__(self):
        return self.title
