from django.test import TestCase
from .models import Categoria


class TextCategoria(TestCase):

    def test_grabacion(self):
        q = Categoria(nombre='Drinks')
        q.save()
        self.assertEqual(Categoria.objects.count(), 1)
