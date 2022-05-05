from django.contrib import admin

# Register your models here.
from.models import Post # we have imported these and put below line so that in admin panel
# we can see our posts and edit them.
admin.site.register(Post)
 
