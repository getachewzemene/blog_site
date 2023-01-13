from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def posts(request):
    # return render(request, 'blog/posts.html')
    pass


def post_detail(request, slug):
    # return render(request, 'blog/post_detail.html')
    pass
