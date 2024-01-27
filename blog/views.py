from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required, user_passes_test


def post_detail(request, pk):
    """
    Renders detailed page.
    """
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    else:
        form = CommentForm()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/post_detail.html", context)


def is_superuser(user):
    """
    Checks if user is superuser.
    """
    return user.is_superuser


@user_passes_test(is_superuser)
def edit_post(request, post_id):
    """
    Edit post.
    """
    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/edit_post.html", {"form": form, "post": post})


@login_required
def delete_comment(request, comment_id):
    """
    Deletes comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:
        comment.delete()

        return redirect("post_detail", pk=comment.post.id)


@user_passes_test(is_superuser)
@login_required
def delete_post(request, post_id):
    """
    Deletes post.
    """
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "blog/delete_post.html", {"post": post})


@user_passes_test(is_superuser)
def add_post(request):
    """
    Adds blog post by superuser.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("post_detail", pk=new_post.id)
    else:
        form = PostForm()

    return render(request, "blog/add_post.html", {"form": form})
