from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register(r'categorias', views.CategoriasViewSet)

urlpatterns = [
    #path('contact/<str:name>/', views.contact, name='contact'),
    #path('categorias/', views.categorias, name='categoria'),
    #path('productos/', views.productoFormView, name='productos'),
    #path('', views.index),
    #path('', include(router.urls))
    path('categorias/', views.CategoriaCreateView.as_view()),
    path('categorias/cantidad/', views.categoria_count),
    path('productos/filtrar/unidades/', views.productos_en_unidades),
    path('productos/reporte/', views.reporte_productos),
]
