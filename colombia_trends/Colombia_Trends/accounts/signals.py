from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_clientes_group(sender, instance, created, **kwargs):
    if created:
        clientes, _ = Group.objects.get_or_create(name='cliente')
        instance.user.groups.add(clientes)
