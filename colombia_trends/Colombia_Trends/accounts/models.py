from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Perfil de usuario


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    apodo = models.CharField(max_length=150, null=True, blank=True, verbose_name='Apodo')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']
        
        
    def __str__(self):
        return self.user.username

    def is_moderator(self):
        """Return True if the user belongs to the 'moderador' group."""
        return self.user.groups.filter(name='moderador').exists()
    is_moderator.boolean = True
    is_moderator.short_description = 'Moderador'
        
        
def create_user_profile(sender, instance, created, **kwargs):   
      if created:
          Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):      
      instance.profile.save()
        
post_save.connect(create_user_profile, sender=User)   
post_save.connect(save_user_profile, sender=User)   
    
    
    
    
        