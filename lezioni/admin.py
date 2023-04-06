from django.contrib import admin
from .models import *

# Register your models here.

class LezioneAdmin(admin.ModelAdmin):
    list_display = ('materia', 'data', 'online')
    search_fields = ('argomento',)


admin.site.register(Lezione, LezioneAdmin)


class IscrizioneInline(admin.TabularInline):
    model = Iscrizione
    extra  = 0

class CorsoAdmin(admin.ModelAdmin):
    inlines = [
        IscrizioneInline,
    ]

admin.site.register(Corso, CorsoAdmin)



admin.site.register(Persona)
admin.site.register(Presenza)

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'corso')
    list_filter = ('corso',)
admin.site.register(Modulo, ModuloAdmin)


class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modulo', 'docente')
    list_filter = ('modulo', 'docente')
admin.site.register(Materia, MateriaAdmin)

class IscrizioneAdmin(admin.ModelAdmin):
    list_display = ('persona', 'corso')
    list_filter = ('corso',)
admin.site.register(Iscrizione, IscrizioneAdmin)