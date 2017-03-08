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
