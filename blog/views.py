from datetime import date
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    try:
        return render(request, 'blog/index.html', {
            "posts": latest_posts,
        })
    except:
        raise Http404("Page does not exist")
        # return HttpResponseNotFound(response_not_found)


def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')

    try:
        return render(request, 'blog/all-posts.html', {
            "posts": posts,
        })
    except:
        raise Http404("Page does not exist")


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    # identified_post = next(post for post in posts if post["slug"] == slug)
    try:
        return render(request, 'blog/post_detail.html', {
            "post": identified_post,
        })
    except:
        raise Http404("Page does not exist")
