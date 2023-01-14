from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.all_posts, name='posts'),
    path('post/<slug:slug>', views.post_detail, name='post-detail'),
]
