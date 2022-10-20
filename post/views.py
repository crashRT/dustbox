from django.shortcuts import render
from .models import PostModel


def postListView(request):
    post_list = PostModel.objects.order_by('posted_at').reverse()
    context = {
        "post_list": post_list,
    }
    return render(request, 'list.html', context)


def postDetailView(request, pk):
    post = PostModel.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, 'detail.html', context)
