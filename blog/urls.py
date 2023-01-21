from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('posts/', views.AllPostListView.as_view(), name='posts'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
]
