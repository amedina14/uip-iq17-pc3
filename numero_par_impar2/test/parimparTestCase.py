"""
Esto es una documentacion con docstring.

clase: parimparTestCase
modulo: test

Este es el modulo para testar las funciones de la clase parimpar
"""
import unittest
from app.parimpar import deducirnumero

class parimparTestCase(unittest.TestCase):
    """
    Esta es la case parimparTestCase para hacer la prueba unitaria de la funcion de la clase parimpar.

    :return:
    """
    def test_deducirnumero(self):
        """
        Esta es la funcion que evalua el parametro pasado por default, si es que es par o impar.

        :return:
        """
        self.assertEquals(deducirnumero(5),"Es impar")

    if __name__=='__main__':
        unittest.main()