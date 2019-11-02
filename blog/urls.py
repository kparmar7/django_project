from django.urls import path
from blog.views import  *
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/',about, name='blog-about'),
]
