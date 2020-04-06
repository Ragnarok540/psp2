import unittest
import lista

class ListaTestCase(unittest.TestCase):

    def test_construir(self):
        esperado = (1, None)
        observado = lista.construir(1)
        self.assertEqual(esperado, observado)

        esperado = (1.5, None)
        observado = lista.construir(1.5)
        self.assertEqual(esperado, observado)

        esperado = (1, (2, None))
        observado = lista.construir(1, lista.construir(2))
        self.assertEqual(esperado, observado)

        self.assertRaises(ValueError, lista.construir, "a")

    def test_lista(self):
        esperado = None
        observado = lista.lista()
        self.assertEqual(esperado, observado)

        esperado = (1, None)
        observado = lista.lista(1)
        self.assertEqual(esperado, observado)
        
        esperado = (1, (2, None))
        observado = lista.lista(1, 2)
        self.assertEqual(esperado, observado)
        
    def test_primero(self):
        l = lista.lista(1, 2, 3)
        esperado = 1
        observado = lista.primero(l)
        self.assertEqual(esperado, observado)

    def test_resto(self):
        l = lista.lista(1, 2, 3)
        esperado = lista.lista(2, 3)
        observado = lista.resto(l)
        self.assertEqual(esperado, observado)

    def test_vacia(self):
        l = lista.lista()
        esperado = True
        observado = lista.vacia(l)
        self.assertEqual(esperado, observado)

        l = lista.lista(1)
        esperado = False
        observado = lista.vacia(l)
        self.assertEqual(esperado, observado)

    def test_largo(self):
        l = lista.lista()
        esperado = 0
        observado = lista.largo(l)
        self.assertEqual(esperado, observado)

        l = lista.lista(1, 2, 3)
        esperado = 3
        observado = lista.largo(l)
        self.assertEqual(esperado, observado)

    def test_sumar(self):
        l = lista.lista()
        esperado = 0
        observado = lista.sumar(l)
        self.assertEqual(esperado, observado)

        l = lista.lista(1, 2, 3)
        esperado = 6
        observado = lista.sumar(l)
        self.assertEqual(esperado, observado)

    def test_mapear(self):
        l = lista.lista(1, 2, 3)
        esperado = lista.lista(1, 4, 9)
        observado = lista.mapear(lambda x: x * x, l)
        self.assertEqual(esperado, observado)

        esperado = lista.lista(0, 1, 2)
        observado = lista.mapear(lambda x: x - 1, l)
        self.assertEqual(esperado, observado)

    def test_zipear(self):
        l1 = lista.lista(1, 2, 3)
        l2 = lista.lista(3, 2, 1)

        esperado = lista.lista(4, 4, 4)
        observado = lista.zipear(lambda x, y: x + y, l1, l2)
        self.assertEqual(esperado, observado)

        esperado = lista.lista(3, 4, 3)
        observado = lista.zipear(lambda x, y: x * y, l1, l2)
        self.assertEqual(esperado, observado)

##    def test_promedio(self):
##        l = psp0.lista()
##        esperado = 0
##        observado = psp0.promedio(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(5)
##        esperado = 5
##        observado = psp0.promedio(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(1, 1.5)
##        esperado = 1.25
##        observado = psp0.promedio(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
##        esperado = 638.9
##        observado = psp0.promedio(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503)
##        esperado = 550.6
##        observado = psp0.promedio(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)
##        esperado = 60.31999999999999
##        observado = psp0.promedio(l)
##        self.assertEqual(esperado, observado)
##
##    def test_desviacion(self):
##        l = psp0.lista()
##        esperado = 0
##        observado = psp0.desviacion(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(5)
##        esperado = 0
##        observado = psp0.desviacion(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
##        esperado = 625.6339806770231
##        observado = psp0.desviacion(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503)
##        esperado = 572.0268447469149
##        observado = psp0.desviacion(l)
##        self.assertEqual(esperado, observado)
##
##        l = psp0.lista(15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)
##        esperado = 62.25583060601187
##        observado = psp0.desviacion(l)
##        self.assertEqual(esperado, observado)
