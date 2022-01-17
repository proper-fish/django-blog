from django import forms
from .models import Post, Comment, Suggested


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class SuggestedForm(forms.ModelForm):
    class Meta:
        model = Suggested
        fields = ('author', 'text',)
