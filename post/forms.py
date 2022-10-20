from .models import PostModel
from django import forms


class add_post(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(add_post, self).__init__(*args, **kwargs)

    class Meta:
        model = PostModel
        fields = ('user', 'user_enc', 'text', 'text_enc', 'posted_at')
        widgets = {'posted_at': forms.HiddenInput()}
        labels = {
            'user': '名前',
            'user_enc': '名前を16進数化',
            'text': '本文',
            'text_enc': '本文を16進数化',
        }
