from django.contrib import admin
from .models import *

# Register your models here.

class LezioneAdmin(admin.ModelAdmin):
    list_display = ('materia', 'data')
    search_fields = ('argomento',)


admin.site.register(Lezione, LezioneAdmin)


admin.site.register(Corso)
admin.site.register(Persona)
admin.site.register(Presenza)

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'corso')
    list_filter = ('corso',)
admin.site.register(Modulo, ModuloAdmin)


class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modulo')
    list_filter = ('modulo',)
admin.site.register(Materia, MateriaAdmin)