from django.db import models
from django.utils import timezone


class PostModel(models.Model):
    user = models.CharField(max_length=20, null=True,
                            blank=True, help_text="名無しでもOK")
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
