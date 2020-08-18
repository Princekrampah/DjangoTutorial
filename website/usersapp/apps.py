from django.apps import AppConfig


class UsersappConfig(AppConfig):
    name = 'usersapp'

    def ready(self):
        from usersapp import signals
