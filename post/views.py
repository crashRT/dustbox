from django.shortcuts import get_object_or_404, redirect, render

from utf8_encode_decode.encode import encodeToUTF8
from .models import PostModel
from .forms import add_post


def postListView(request):
    posts_list = PostModel.objects.order_by('posted_at').reverse()
    context = {
        "posts_list": posts_list,
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
            obj = form.save(commit=False)
            if obj.user_enc:
                obj.user = encodeToUTF8(obj.user)
            if obj.text_enc:
                obj.text = encodeToUTF8(obj.text)
            obj.save()
            return redirect('post_list')
    else:
        form = add_post()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)
