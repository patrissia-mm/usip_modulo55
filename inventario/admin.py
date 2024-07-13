from django.contrib import admin
from .models import Categoria, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'unidades', 'disponible', 'created', 'updated')
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre',)
    ordering = ('precio',)

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
