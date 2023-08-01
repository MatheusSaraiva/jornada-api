from django.db import models


class Destino(models.Model):
    preco = models.FloatField()
    nome = models.CharField(max_length=255)
    foto1 = models.ImageField(upload_to='fotos', null=True, blank=True)
    foto2 = models.ImageField(upload_to='fotos', null=True, blank=True)
    meta = models.CharField(max_length=160,)
    text_descritivo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome