"""
Esto es una documentacion con docstring.

clase: mainTestCase
modulo: test

Este es el modulo para testar las funciones de la clase parimpar
"""
import unittest
from app.maxmin import max_val, min_val

class maxminTestCase(unittest.TestCase):
    def test_min_val(self):
        self.assertEqual(min_val(10, 25), 10)

    def test_max_val(self):
        self.assertEqual(max_val(10, 25), 25)


if __name__ == '_main_':
    unittest.main()