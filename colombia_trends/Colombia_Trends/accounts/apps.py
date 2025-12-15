from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Perfiles'
    
    def ready(self):
        # Import signals with a relative import to avoid import issues
        from . import signals  # noqa