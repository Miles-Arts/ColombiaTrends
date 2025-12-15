from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile


@receiver(post_save, sender=Profile)
def add_user_students_gruop(sender, instance, created, **kwargs):
    