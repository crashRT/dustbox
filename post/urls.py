from django.contrib import admin
from django.urls import path
from post.views import postListView, postDetailView, postAddView, ApiGoodView, postTopView


urlpatterns = [
    path('', postTopView, name='post_top'),
    path('list/<int:pk>/', postListView, name='post_list'),
    path('detail/<int:pk>/', postDetailView, name='post_detail'),
    path('add', postAddView, name='post_add'),
    path('api/good/<int:pk>/', ApiGoodView, name='api_good'),
]
