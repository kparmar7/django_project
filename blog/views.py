from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView )
from django.contrib.messages.api import success



def home(r):
    context={
        'p':Post.objects.all(),
        'title':'HOME',
        }
    return render(r, 'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='p'
    ordering=['-date_posted']
    paginate_by=2
    
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name='p'
    paginate_by=2
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model=Post

class PostCreateView( LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
def about(r):
    return render(r, 'blog/about.html',{'title':'ABOUT'})








"""
>>> from django.core.paginator import Paginator
>>> posts=['1','2','3','4','5']
>>> p=Paginator(posts,2)
>>> p.num_pages
3
>>> for page in p.page_range:
...     print(page)
...
1
2
3
>>> p1=p.page(1)
>>>
>>> p1
<Page 1 of 3>
>>> p1.number
1
>>> p1.object_list
['1', '2']
>>> p1.has_previous()
False
>>> p1.has_next()
True
>>> p1.next_page_number()
2
>>> exit()"""