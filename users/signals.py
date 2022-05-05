from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# below code explanation corey schafer python django web app video 8 minute 31
@receiver(post_save, sender=User) # first argument is signal, second arg is sender.when user is saved, send this signal. this signal is going to be receieved by the receiver. receiver is this create_profile function.
def create_profile(sender, instance, created, **kwargs): #  all arguments passed by post_save signal.
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

    # then go to users.apps.py
