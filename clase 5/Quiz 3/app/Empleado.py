class Empleado:
    conteo = 0 #variable global modificable por cada objeto, los dos guines bajos son para privados.

    def __init__(self, nombre, salario): #Self es para usar atributos/variables de la misma clase. Por lo general TIENE que ir...
        self.nombre = nombre              #"""esto es el costructor"""
        self.salario = salario
        Empleado.conteo += 1

    def mostrar_conteo(self):
        print("Esta empresa tiene "+ str(Empleado.conteo) + " empleado.")

    def mostrar_empleado(self):
        print("Nombre: " + self.nombre)
        print("Salario: " + str(self.salario))

    def calcular_salario_neto(self):
        if self.salario < 2000:
            return self.salario*0.93
        elif self.salario > 5000:
            return self.salario * 0.85
        else:
            return  self.salario

#            return self.salario
