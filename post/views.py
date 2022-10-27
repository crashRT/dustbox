from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.http.response import JsonResponse

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
            if not obj.user:
                obj.user = "どこかのだれか"
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
                'notice': '不正な入力です',
            }
            return render(request, 'form.html', context)
    else:
        form = add_post()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)


def ApiGoodView(request, pk):
    try:
        obj = PostModel.objects.get(pk=pk)  # pkを元にPostテーブルの対象記事レコードを取得する
    except PostModel.DoesNotExist:
        raise Http404
    obj.good += 1  # ここでいいねの数を増やす
    obj.save()  # 保存をする

    return JsonResponse({"good": obj.good})  # いいねの数をJavaScriptに渡す
