from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_group(sender, instance, created, **kwargs):
    clientes, _ = Group.objects.get_or_create(name='cliente')
    moderadores, _ = Group.objects.get_or_create(name='moderador')
    admins, _ = Group.objects.get_or_create(name='admin')

    if instance.is_moderator():
        instance.user.groups.add(moderadores)
    elif instance.user.is_staff or instance.user.is_superuser:
        instance.user.groups.add(admins)
    else:
        instance.user.groups.add(clientes)