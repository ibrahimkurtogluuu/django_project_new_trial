from django.db import models
from django.contrib.auth.models import User # first inherited User model.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # ONE TO ONE relationship user can have one profile and profile can have one user.
    # on delete means when delete profile user wont be deleted. but delete user profile will be deleted.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        # whenever we print out profile it will give 'username profile'

        # after doing it in cmd python manage.py makemigrations.
        # when did that it will create us profile model.
        # for running the migrations to updata the database
        # python manage.py migrate
        # to be able to see users profile page we need to register profile model in users/admin.py
        # when go to admin page you will see profile section.
        # we can create a new profile manually.
        # create ibrahim profile with selecting a picture.
        # create TestUser profile without selecting a picture.
        #
        # and go to NOTES3.py
