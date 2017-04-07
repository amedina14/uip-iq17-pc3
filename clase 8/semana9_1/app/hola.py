#clase Hola, modulo hola
"""
Esto es una documentacion con docstring.

clase: Hola
modulo: hola

Este es el modulo para saludar

"""

class  Hola(object):
    """

    Esta es la clase Hola para encapsular un saludo. (las documentaciones van inmediatamente despues de la definicion.
    """
    def __init__(self, nombre):
        """
        Este es el constructor.

        Crea una instacia de la :class:'Hola'

        :param nombre:
        :type nombre: str
        """

        self.nombre = nombre

    def saludar(self):
        print("Hola %s" % self.nombre)