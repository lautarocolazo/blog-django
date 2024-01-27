from django.shortcuts import render
from blog.models import BlogPost, Comment


def home_page(request):
    """
    Rendering home page
    """

    posts = BlogPost.objects.all()
    comments = Comment.objects.all()

    context = {"posts": posts, "comments": comments}
    return render(request, "home.html", context)
