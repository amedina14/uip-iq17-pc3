'''
Quiz 1:
Hacer un programa que lea una temperatura en farenheit y la convierta en celsius y si es mayor
a 100°C imprima "caliente". Si es menor a 0°C imprima "frio"
'''

tempF = int(input("TempF: "))

#(tempF - 32/(5/9))
tempC = (((tempF - 32)*5)/9)

print("\nLa temperatura en Celsius es " + str(tempC))

if tempC >= 100:
	print("caliente")
elif tempC < 0:
	print("frio")