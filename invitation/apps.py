from django.apps import AppConfig


class InvitationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invitation'

    def ready(self):
        from . import receivers
