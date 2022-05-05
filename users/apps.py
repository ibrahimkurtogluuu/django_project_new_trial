from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
    


# to create an app like such as blog, users,
# put 'python manage.py startapp users' in command line. users is the name of the app.
# and add class name 'UsersConfig' in INSTALLED_APPS  in django_project/settings.py .
