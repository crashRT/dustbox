from django.db import models
from django.utils import timezone


class PostModel(models.Model):
    user = models.CharField(max_length=20, null=True,
                            blank=True, help_text="名無しでもOK")
    user_enc = models.BooleanField(help_text="名前を16進数化するかどうか")
    text = models.TextField()
    text_enc = models.BooleanField(help_text="投稿内容を16進数化するかどうか")
    posted_at = models.DateTimeField(default=timezone.now)
