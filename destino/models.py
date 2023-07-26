from django.db import models


class Destino(models.Model):
    preco = models.FloatField()
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    def __str__(self):
        return self.nome