import unittest
from prueba_unitaria1.app.circunferencia import circunferencia

class CircunferenciaTestCase(unittest.TestCase):
    def setUp(self):
        self.circunferencia = circunferencia(5)

    def test_calcular_area(self):
        #dependiendo del codigo se unsan los assert respectivamente
        self.assertEqual(self.circunferencia.calcular_area(), 78.54, "Esto se muestra si no es igual: Radio incorrecto")

    def test_calcular_diametro(self):
        #dependiendo del codigo se unsan los assert respectivamente
        self.assertEqual(self.circunferencia.calcular_diametro(), 10.0, "Esto se muestra si no es igual: Diametro incorrecto")