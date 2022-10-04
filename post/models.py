from django.db import models
from django.utils import timezone

# Create your models here.


class PostModel(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
