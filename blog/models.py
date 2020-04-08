from django.db import models

from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')