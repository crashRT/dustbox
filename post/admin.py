from django.contrib import admin

# Register your models here.
from .models import PostModel


@admin.register(PostModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
