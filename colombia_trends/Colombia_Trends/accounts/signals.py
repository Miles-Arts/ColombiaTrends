from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_group(sender, instance, created, **kwargs):
    if created:
        clientes, _ = Group.objects.get_or_create(name='cliente')
        admins, _ = Group.objects.get_or_create(name='admin')
        # Ejemplo: asignar por username
        if instance.user.username == 'admin':
            instance.user.groups.add(admins)
        else:
            instance.user.groups.add(clientes)