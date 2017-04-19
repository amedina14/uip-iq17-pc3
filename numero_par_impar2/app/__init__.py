"""
Este es el Init que devuelve los objetos y el resultado

"""
from app.parimpar import deducirnumero

if __name__ == "__main__":

    enunciado = """
    Desarrolle un programa de línea de comandos, basado en funciones, que dado un número identifique si el mismo es par o impar.
    Para dicho programa cree una clase de pruebas utilizando el framework unittest y ejecute las pruebas unitarias correspondientes.
    """
    print(enunciado)

    numero = int(input("Ingresa un numero: "))
    print(deducirnumero(numero))






