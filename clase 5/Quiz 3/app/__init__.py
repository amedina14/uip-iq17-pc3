from app.Empleado import Empleado  #en from ya declaro el modulo
from app.Ejecutivo import Ejecutivo

if __name__== "__main__":

print("***Menu***")


def menu():
    print("\tAgregar empleado y ejecutivo 1: ")
    print("\tMostrar 2: ")
    print("\tSalir 3: ")

flag = True
listae = []

while(flag):
        menu()
        try:
            op = input('Eliga una opcion:... \n')
        except:
            print("error general")
        if op == "1":

            ne = input("ingresa nombre empleado: ")
            se = input("ingresa salario empleado: ")
            listae.append(Empleado()) # esto esta bien, Solo hay que modificar el __init__

            nex = input("ingresa nombre ejecutivo: ")
            sex = input("ingresa salario ejecutivo: ")
            listaex= [nex,sex]
            e1= Empleado(listae)


        if op == "2":
            print("Informacion de Empleados")
            e1.mostrar_empleado()

            print("Informacion de ejecutivos")
            ex1 = Ejecutivo(listaex)  # creo OBJETO de clase EJECUTIVO

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
'''



    1
    ingesar
    cin >> x
    e1.Emplado(no, sal)
    ex1.E...

    if 2
        muestra
'''
