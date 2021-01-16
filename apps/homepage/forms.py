from django import forms

from .models import Comment
from .models import Post
from .models import PostImage


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update(
            {"autofocus": "autofocus", "placeholder": "Add a comment..."}
        )
        # this overwrites the input for content field and lets you update attrs of that input <input>


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ["modelimage"]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)
