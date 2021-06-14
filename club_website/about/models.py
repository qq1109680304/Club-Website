from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AboutPage(models.Model):
    title1 = models.CharField(max_length=100)
    text1 = models.TextField()
    title2 = models.CharField(max_length=100)
    text2 = models.TextField()
    title3 = models.CharField(max_length=100)
    text3 = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)