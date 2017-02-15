from app.Empleados import Empleados

class Ejecutivo(Empleados): #Para trabajar con HERENCIA coloco el nombre de la clase padre
    def mandar(self):
        print("Traeme un cafe!")


    def calcular_salario_neto(self):
        return  self.__salario * 0.98

    def mostrar_empleado(self, saludo):
        print("Nombre: {} {}".format(saludo,self.__nombre)) #abria que hacerlos gets
        print("Salario: " + str(self.__salario))