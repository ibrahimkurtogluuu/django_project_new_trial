from django.db import models
from django.utils import timezone # to make timezone below line in data_posted object
from django.contrib.auth.models import User # user is also a model or class but
# since user is goint to be the author of the posts these two are relational.
# one to many relation. user can have many posts but post can have one user.
# Create your models here. we are going to make post models(classes). ORM.
# object relational matters. each class is going to be its own tables and databases.

from django.urls import reverse # N5

class Post(models.Model): # each class is going to be its own tables and databases. Instances of class are posts.
    title = models.CharField(max_length=100)# these are fields or variables: title. content ...
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add = True) # current time when object is created.
# but if did say auto_now it will give us current normal time.
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):# this function gives title of models when we see all the objects of this class
        return self.title
#author is User. User and Post are different databases and relational. if we on_delete
# delete user CASCADE means posts will be deleted. but if you delete posts users wont
# be deleted. one way.
#N5
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # N5 keyword arguments are values that, when passed into a function, are identifiable by specific parameter names

#N5
# we need to run migrations on cmd to update the database we changed.
# with this command python manage.py makemigrations
# then blog/migrations/0001_initial.py generated. this document is sql code.
# when we run this document it will generate us databases for moduls.
# to run it easily we need to run "python manage.py sqlmigrate blog(app name) 0001(migration number)" code in cmd.
# then put "python manage.py migrate" command. and changes have been made in database.
# to make query in database we need run python manage.py shell
# put from blog.models import Post
# put from django.contrib.auth.models import User

# then for some query:
# put User.objects.all(),   User.objects.first(),  User.objects.last()
# User.objects.filter(username="İbrahim") it could give me multiple result with ibrahim names
# for unique result User.objects.filter(username="ibrahim").first()
# catch it in a variable put "user = User.objects.filter(username='ibrahim')"
# for name put user, for user id put user.id for primary_key put user.pk
# put user= User.objects.get(id=1) just made the user has id number is equal to 1 is user.basically same user.
# so now user variable is equal to ibrahim
# Post.objects.all() it gives us empty list. because there is no post.
# lets make one post and assign user as the author of this post
# post_1 = Post(title="Blog 1", content="First Post Content!", author=user)
# we didnt give data_posted so by default it will give us current update time.
# because we have already made that.
# Post.objects.all() it will give us emty list again. why? because we created a post_1 object
# but we didnt save it. to do it: we put post_1.save()
# in order to see class objects with their titles we need use a dunder method in models.py
# above code in class Post we put a method.
# exit() the shell. rerun the shell python manage.py shell
# and import models again with "from django.contrib.auth.models import User" and
# "from blog.models import Post" and put Post.objects.all() output is below explained:
### before putting that function(dunder) it gave us "<QuerySet [<Post: Post object (1)>]>"
# now it gives us "<QuerySet [<Post: Blog 1>]>" with Blog 1 title.

# when i exit and rerun the shell again we lose user variable.
# we need to create it again. and then create a post_2 and make the author of this post
# is the user. something different:use "author_id=user.id"
# now we have two posts.

# put post = Post.objects.first()
# put post.content
# since when we put post.author it gives us entire User object. such as <User: ibrahim>
# when we say post.author.email it gives us users mail.

# to know what are the posts that were written by spesific user
# put user.post_set, user.post_set.all()
# since it gives us <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
# to make a new post that is written by user. put user.post_set.create(title="Blog 3", content = "Third Post Content!")
# with this command we didnt need to specify the author and save.

# how to use these posts instead of dummy data. and edit these data in admin pages
# exit() the shell.
# go to views.py first put from .models import Post and change 'posts': "postas with Post.objects.all()"
#
