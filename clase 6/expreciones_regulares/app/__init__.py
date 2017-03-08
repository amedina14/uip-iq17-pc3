import  re

if __name__=="__main__":
    c1="casa"
    c2="casas"
    c3="pasa"

    c4=input("ingresa un texto: ")

    if re.match(c1,c2):
        print("1 casa y casas coinciden")
    else:
        print("1 casa y casas no coinciden")

    if re.match(c1, c3):
        print("2 casa y pasa coinciden")
    else:
        print("2 casa y pasa no coinciden")

    #comodin, sustituye caracteres a-z y numeros..
#    if re.match(".asa", c1):
 #       print("coincide")

    print("PRUEBAS CON EXPRESIONES REGULARES")

    if re.match(".asa", c4):
      print("3 coincide")
    else:
        print("3 no coincide")

    if re.match("\.py", c4):
        print("4 archivo encontrado")
    else:
        print("4 archivo no encontrado")

#validar algo en un campo tenga formato espeficicon(que tenga certa cantidad de numeros.) [a-z A-Z]
    if re.match("jpg|png|gif", c4):
        print("5 Tipo de archivo encontrado")
    else:
        print("5 No encontrado")

    if re.match("ca(..|...)ta", c4):
        print("6 Encontrado")
    else:
        print("6 No encontrado")

"""    if re.match("ma(s|m|n)a", c4):
        print("7 Es masa mama o mana")
    else:
        print("7 No es masa mama o mana")
"""

palabras = ['mama','mata','mara','mana']
for p in palabras:

         if re.match("ma(s|m|n)a", p):
            print("8 Es masa mama o mana")
         else:
            print("8 No es masa mama o mana")

if re.match('r2d\-[0-5]', c4):
    print("9 Hola")
else:
    print("9 Adios")

#if re.match('c3p[0-3a-c]', c4):
#    print("10 Sup")
#else:
#    print("10 Bye")

#NB: fullmatch cadena igual al patron.

if re.fullmatch('c3p[0-3a-zA-Z]', c4):
    print("11 Sup")
else:
    print("11 Bye")


if re.fullmatch('a1[.:]', c4):
    print("12 Coincide")
else:
    print("12 No coincide")

#caracteres predefinidos
#\d numeros
#\D no numeros
#\w palabras
#\W no palabras
#\s espacios en blacon
#\S no espacios en blanco

if re.fullmatch('ho\d', c4):
    print("13 Jo")
else:
    print("13 Ju")

#+ 1 o mas
#* 0 o mas
#? 0 o 1
#{} num o rango de las veces que puede aparecer

if re.fullmatch("A[a-z]+", c4):
    print("14 Es un nombre que inicia con A")
else:
    print("14 No coincide")

#match coincida el inicio de la palabra con el patron y fullmatch exactamente igual el inicio y la cantidad.
#match lo busca al inicio de la linea, ful completa, search en cualquier parte
if re.fullmatch("[A-Z]+[a-z]*\s[1-9]{1,3}", c4):
    print("15 Valido")
else:
    print("15 No Valido")

#Search: Busca la string en cualquier lugar de la palabra.
# ^(circunflejo) inicio forzado de la string
# $ fin forzado string

if re.search("^[a-z]{1,3}",c4):
    print("16 Sirve")
else:
    print("16 No sirve")

if re.search("^http://",c4):
    print("17 URL")
else:
    print("17 No URL")

if re.search("\.es$",c4):
    print("18 Sitio en espaniol")
else:
    print("18 No esta en espanol")

if re.search("^http://[a-z]{3}\.[a-z]+\.[a-z]*$",c4):
    print("19 Terminamos bien link")
else:
    print("19 Indirizzo errato")


