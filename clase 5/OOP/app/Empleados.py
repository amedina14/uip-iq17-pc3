class Empleados:
    __conteo = 0 #variable global modificable por cada objeto, los dos guines bajos son para privados.

    def __init__(self, nombre, salario): #Self es para usar atributos/variables de la misma clase. Por lo general TIENE que ir...
        self.__nombre = nombre              #"""esto es el costructor"""
        self.__salario = salario
        Empleados.__conteo += 1

    def mostrar_conteo(self):
        print("Esta empresa tiene "+ str(Empleados.__conteo) + " empleado.")

    def mostrar_empleado(self):
        print("Nombre: " + self.__nombre)
        print("Salario: " + str(self.__salario))

    def calcular_salario_neto(self):
        if self.__salario < 2000:
            return self.__salario*0.93
        elif self.__salario > 5000:
            return self.__salario * 0.85
        else:
            return  self.__salario

#            return self.salario
