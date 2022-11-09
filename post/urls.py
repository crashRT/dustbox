from django.contrib import admin
from django.urls import path
from post.views import postListView, postAddView, ApiGoodView, postTopView


urlpatterns = [
    path('', postTopView, name='post_top'),
    path('list/<int:index>/', postListView, name='post_list'),
    path('add', postAddView, name='post_add'),
    path('api/good/<int:pk>/', ApiGoodView, name='api_good'),
]
