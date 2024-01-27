from django import forms
from .models import BlogPost, Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-3 text-sm focus:outline-none focus:border-black",
                "placeholder": "Your comment here",
            }
        ),
        label="Comment",  # Add a label
    )

    class Meta:
        model = Comment
        fields = ["content"]


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-3 text-sm focus:outline-none focus:border-black",
            }
        ),
    )

    content = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-3 text-sm focus:outline-none focus:border-black",
            }
        ),
    )

    class Meta:
        model = BlogPost
        fields = ["title", "content"]
