from django.db import models
from django.contrib.auth.models import User

# Perfil de usuario


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    apodo = models.CharField(max_length=150, null=True, blank=True, verbose_name='Apodo')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    
    class Meta:
        verbo_name = 'perfil'
        verbo_name = 'perfiles'
        