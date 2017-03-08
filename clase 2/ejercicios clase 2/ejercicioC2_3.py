mensaje = '''
        Es un mensaje de
        varias lineas y
        no me interesa lo que falte.
        Chao
        '''

sal = True

#while sal: (asume la verdad booleana)
while sal == True:
    nombre = input("Nombre: ")
    notafinal = int(input("nota final: "))

    if 91 <= notafinal <= 100:
        print(nombre + ", sacaste una A (" + str(notafinal) + ")!")
    elif notafinal >= 81:
        print(nombre + ", sacaste una B (" + str(notafinal) + ")!")
    elif notafinal >= 71:
        print(nombre + ", sacaste una C (" + str(notafinal) + ")!")
    else:
        if notafinal < 0:
            print("nota final invalida")
        else:
            print(nombre + ", sacaste una F (" + str(notafinal) + ")!")
    opcion = input("Desea continuar (S/N)? ").upper()

    if opcion == 'N':
        sal = False
        print("Hasta luego")
    elif opcion == 'S':
        sal = True
    else:
        sal = True
        print("No colocaste algo valido, pero te mantendre en el ciclo")

print(mensaje)
