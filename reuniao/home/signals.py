from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Usuarios


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="criar_ou_atualizar_usuarios")
def criar_ou_atualizar_usuarios(sender, instance, created, **kwargs):
    if created:
        Usuarios.objects.create(
            usuario=instance,
            mail=instance.email,
        )
    else:
        Usuarios.objects.filter(usuario=instance).update(
            mail=instance.email,
        )