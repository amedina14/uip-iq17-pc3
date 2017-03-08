from app.Empleado import Empleado


class Ejecutivo(Empleado):  # Para trabajar con HERENCIA coloco el nombre de la clase padre
    def mandar(self):
        print("Traeme un cafe!")

    def calcular_salario_neto(self):
        return self.salario * 0.98

    def mostrar_empleado(self):
        print("Nombre: "+ self.nombre)
        print("Salario: "+ str(self.salario))

#        print("Nombre: {} {}".format(saludo, self.nombre))
