from app.Empleados import Empleados  #en from ya declaro el modulo
from app.Ejecutivo import Ejecutivo
import time

if __name__== "__main__":
    # este es el main
    print(__name__)
    # Paso los parametros... 1 Modulo, 2 Clase, 3 Parametro
    e1 = Empleados("Juan", 2500)
    # Creo el segundo objeto
    e2 = Empleados("Maria", 4250)
    #print("Empleados Totales: " + str(Empleados.__conteo))
    e1.mostrar_conteo()

    print("Informacion de Empleados")
    e1.mostrar_empleado()
    e2.mostrar_empleado()

    # creo OBJETO de clase EJECUTIVO
    ex1 = Ejecutivo("Petra", 15000)
    # creo OBJETO de clase EJECUTIVO, Y OVERLOAD le paso el parametro SALUDO para visualizar el atributo xq es privado
    ex1.mostrar_empleado("Sr(a)")
    ex1.mostrar_conteo()
    ex1.mandar()
    ex1_salario_neto = ex1.calcular_salario_neto()

    #modo mejor: {}metodo nuevo ,{:.3f}metodo viejo, aqui le doy 3 dec por ejemplo
    #print("El Sr(a). {} tiene salario neto de ${:.2f}".format(ex1.__nombre, ex1_salario_neto))
    e2_salario_neto = e2.calcular_salario_neto()

    # modo mejor: {}metodo nuevo ,{:.3f}metodo viejo, aqui le doy 3 dec por ejemplo
    #print("El Sr(a). {} tiene salario neto de ${:.2f}".format(e2.nombre,e2_salario_neto))

#    print("El Sr(a)." + ex1.nombre +" tiene salario neto" + str(ex1_salario_neto))   #modo 1
#    print("El Sr(a). %s tiene salario neto de $%2f." % (ex1.nombre, ex1_salario_neto))    #modo 2

    #time.sleep(10)       #este es una mala practica porque mato el objeto
    #del e2
    #e2.mostrar_empleado()