from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def all_posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request, slug):
    # return render(request, 'blog/post_detail.html')
    pass
