from app.Empleados import Empleados

#Para trabajar con HERENCIA coloco el nombre de la clase padre
class Ejecutivo(Empleados):
    def mandar(self):
        print("Traeme un cafe!")


    def calcular_salario_neto(self):
        return  self.salario * 0.98

    def mostrar_empleado(self, saludo):
        # Para imprimir atributos privados habria que hacerlos metodos gets.
        print("Nombre: {} {}".format(saludo,self.nombre))
        print("Salario: " + str(self.salario))