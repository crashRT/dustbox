from django.shortcuts import get_object_or_404, redirect, render
from .models import PostModel
from .forms import add_post


def postListView(request):
    posts_list = PostModel.objects.order_by('posted_at').reverse()
    context = {
        "post_list": posts_list,
    }
    return render(request, 'list.html', context)


def postDetailView(request, pk):
    post = PostModel.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, 'detail.html', context)


def postAddView(request):
    if request.method == 'POST':
        form = add_post(request.POST)
        if form.is_valid():
            # if form.data['user_enc']:
            # encrypt user name
            form.save()
            return redirect('post_list')
    else:
        form = add_post()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)
