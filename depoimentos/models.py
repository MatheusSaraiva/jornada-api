from django.db import models


class Depoimento(models.Model):
    depoimento = models.CharField(max_length=150)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    def __str__(self):
        return self.depoimento