from django.contrib import admin
from django.urls import path
from post.views import postListView, postDetailView

urlpatterns = [
    path('', postListView, name='post_list'),
    path('detail/<int:pk>/', postDetailView, name='post_detail'),
]
