from django.contrib import admin

from destino.models import Destino


class Destinos(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id',)

admin.site.register(Destino, Destinos)