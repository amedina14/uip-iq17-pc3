print("***Menu***")

def menu():
    print("\tOpcion 1")
    print("\tOpcion 2")
    print("\tOpcion 3")

flag = True

while(flag):
        menu()
        try:
            op = input('Eliga una opcion:... \n')
        except:
            print("error general")
        if op == "1":
            print("Hola")
        if op == "2":
            archivo = open("quiz2.txt",'a')
            archivo.write("Hola prof;\n")
            archivo.close()

        if op == "3":
            flag = False
            print("Chao prof")
            break





