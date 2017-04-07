"""
Modulo inicial de persona
"""

class  Persona(object):
    """

    Esta es la clase Persona de un ciudadano del mundo
    """
    def __init__(self, nombre, edad):
        """
        Este es el constructor.

        Crea una instacia de la :class:'Hola'

        :param nombre:
        :type nombre: str
        """

        self.nombre = nombre

    def saludar(self):
        print("Hola %s" % self.nombre)

    def votar