from prueba_unitaria1.app.circunferencia import circunferencia

if __name__=="__main__":
    radio = float(input("Radio: "))
    c1 = circunferencia(radio)
    c1_area = c1.calcular_area()
    c1_diametro = c1.calcular_diametro()
    print("Area: "+ str(c1_area))
    print("Diametro: "+ str(c1_diametro))
