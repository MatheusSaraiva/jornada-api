from django.db import models

from destino.bard import bard_descritivo


class Destino(models.Model):
    preco = models.FloatField()
    nome = models.CharField(max_length=255)
    foto1 = models.ImageField(upload_to='fotos', null=True, blank=True,)
    foto2 = models.ImageField(upload_to='fotos', null=True, blank=True)
    meta = models.CharField(max_length=160,)
    text_descritivo = models.CharField(max_length=500, null=True, blank=True,  default=None)

    def __str__(self):
        return self.nome
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.text_descritivo is None or self.text_descritivo == "":
            self.text_descritivo = bard_descritivo(self.nome)
        if update_fields is not None and "nome" in update_fields:
            update_fields = {"text_descritivo"}.union(update_fields)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )