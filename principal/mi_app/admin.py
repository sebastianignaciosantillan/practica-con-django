from django.contrib import admin
from .models import *
# Register your models here.


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad')
    
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_publicacion', 'genero') 
    
admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)   
admin.site.register(Galeria)    