from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

# admin bulunan yeri boş yaptık ki path içerisindeki ilk variable ı admine değilde
# home page a gitsin.

# first creating this blog app, this url.py document was empty.we have put above importing codes.
# from. means in this directory(in blog directory) go to views.py document and import functions in views
# document so that we can use views.home, views.about functions down below.
# we have imported path, we put url urlpatterns. Requests goes to urls.py in django_project.
# and then comes here with "path('', include('blog.urls')". from here they go to views.py.
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # N5 changed views.home with PostListView.as_view() PostListView has to be converted into a view. thats why we used as_view() function #
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # N5 when user goes to post/1 it will take user to blog 1.
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path("about/", views.about, name='blog-about'),
]
