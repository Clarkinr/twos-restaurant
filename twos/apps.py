"""
registers the django app twos
"""
from django.apps import AppConfig


class TwosConfig(AppConfig):
    """
    registers the app name
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twos'
