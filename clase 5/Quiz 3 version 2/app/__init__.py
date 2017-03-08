#en from ya declaro el modulo
from app.Empleado import Empleado
from app.Ejecutivo import Ejecutivo

if __name__== "__main__":

 print("***Menu***")


def menu():
    print("\tAgregar empleado y ejecutivo 1: ")
    print("\tMostrar 2: ")
    print("\tSalir 3: ")

flag = True
listae = []
listaex = []

while(flag):
        menu()
        try:
            op = input('Eliga una opcion:... \n')
        except:
            print("error general")
        if op == "1":

            ne = input("ingresa nombre empleado: ")
            se = input("ingresa salario empleado: ")
            listae.append(Empleado(ne,se)) # esto esta bien, Solo hay que modificar el __init__

            nex = input("ingresa nombre ejecutivo: ")
            sex = input("ingresa salario ejecutivo: ")
            # esto esta bien, Solo hay que modificar el __init__
            listaex.append(Ejecutivo(nex, sex))

#e1= Empleado(listae)


        if op == "2":
            print("Informacion de Empleados")
            for i in range (0,len(listae)):
                listae[i].mostrar_empleado()

            print("Informacion de ejecutivos")
            for j in range (0, len(listaex)):
                listaex[j].mostrar_empleado()

  #              ex1 = Ejecutivo(listaex)  # creo OBJETO de clase EJECUTIVO

        if op == "3":
            flag = False
            print("Chao prof")
            break














'''        if()

            ex1= emp(lista)
        else:
'''

'''archivo = open("quiz2.txt",'a')
archivo.write("Hola prof;\n")
archivo.close()'''




    1
    ingesar
    cin >> x
    e1.Emplado(no, sal)
    ex1.E...

    if 2
        muestra
'''
