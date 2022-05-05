from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView# N5
)
from django.contrib.auth.models import User
from .models import Post
# with above importing we could use down below "return HttpResponse" in "def about" function
# so that any request with http://127.0.0.1:8000/about comes from users will be put in def about function
# then "Blog About" string will be shown to them.
# BUT!
# we are using something different now.
# we are rendering. and for rendering we run html files in the subdirectory in directory that views.py in
#

postas = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
# N5
class PostListView(ListView):
    model = Post # this will tell our ListView which model to query in order to create the list
    template_name =  'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # by putting - sign before date_posted. newest to oldest.
    paginate_by = 5

# N6
class UserPostListView(ListView):
    model = Post # this will tell our ListView which model to query in order to create the list
    template_name =  'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# get object from User model that has a username equals username from get URL.
# if User model has an object named as the same username as in URL so that means
# it will capture it in user. if it doesnt exist it will raise
# 404 error.
# when we capture User object in user we will limit it by saying
# we will say that just return the posts that has the author equals user.

# N6
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
# N5
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#def about(request):
#    return HttpResponse("<h1>Blog About</h1>")

# above function we could show in html file "Blog About" string.
# request comes in urls.py in django_project then goes to urls.py in blog
# why any request comes with "http://127.0.0.1:8000/about" goes to urls.py in blog app
# because we have put "path('', include('blog.urls')" in urlpatterns in urls.py in django_project directory
