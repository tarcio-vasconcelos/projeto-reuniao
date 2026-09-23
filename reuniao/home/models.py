from django.db import models
from django.conf import settings

# Create your models here.
class Usuarios(models.Model):
    class Papel(models.TextChoices):
        EXTERNO = "EXTERNO", "Externo"
        EP = "EP", "Ep"

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil",
    )

    mail = models.EmailField(blank=True)

    setor = models.CharField(max_length=200, blank=True)
    area = models.CharField(max_length=200, blank=True)
    papel = models.CharField(
        max_length=100,
        choices=Papel.choices,
        default=Papel.EXTERNO,
    )
    peso = models.IntegerField(default=0)

    def __str__(self):
        return f"Usuario: {self.usuario}"