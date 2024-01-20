from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment


def post_detail(request, pk):
    """
    Renders detailed page
    """
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {"post": post, "comments": comments}
    return render(request, "blog/post_detail.html", context)
