from datetime import date
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Post
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostListView(ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset
        return data


class PostDetailView(View):
    # model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_stored_post = post_id in stored_posts
        else:
            is_stored_post = False
        return is_stored_post

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': form,
            'comments': post.comments.all().order_by('-created_at'),
            'is_stored_post': self.get_stored_post(request, post.id),
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=[slug]))
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': form,
            'comments': post.comments.all().order_by('-created_at'),
            'is_stored_post': self.get_stored_post(request, post.id),
        }
        return render(request, self.template_name, context)


class ReadLater(View):
    template_name = "blog/stored_post.html"

    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        return render(request, self.template_name, context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST['post_id'])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts
        return HttpResponseRedirect("/")
