from django.contrib import admin

from depoimentos.models import Depoimento


class Depoimentos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'depoimento')
    list_display_links = ('id',)

admin.site.register(Depoimento, Depoimentos)