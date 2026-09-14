from django.db import models

# Create your models here.
class Usuarios(models.Model):
    class Papel(models.TextChoices):
        EXTERNO = "EXTERNO", "Externo"
        EP = "EP", "Ep"

    usuario = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    setor = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    papel = models.CharField(
        max_length=100,
        choices=Papel.choices,
        default=Papel.EXTERNO,
    )
    peso = models.IntegerField()

    def __str__(self):
        return f"Usuario: {self.usuario}"