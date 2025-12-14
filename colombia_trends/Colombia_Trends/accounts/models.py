from django.db import models
from django.contrib.auth.models import User

# Perfil de usuario


class Profile(models.Model):
    user = models.OneToOneField(User,)
