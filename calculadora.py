seleccionar = 0
while seleccionar != 8:
    numero1 = int(input("Introduzca el primer numero: "))
    numero2 = int(input("Introduzca el segundo numero: "))
    print("""
        Indique la operación a realizar :
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Raiz Cuadrada
        6. Potenciacion
        7. Cambiar numeros
        8. Salir de la calculadora
          """)

    eleccion= int(input(""))
    if eleccion == 1:
            print("")
            print("Resultado:" , numero1 ,"+", numero2, "=", numero1 + numero2)
    elif eleccion == 2:
            print("")
            print("Resultado: ", numero1 ,"-", numero2, "=", numero1 - numero2)
    elif eleccion == 3:
            print ("")
            print ("Resultado: ", numero1, "*", numero2, "=", numero1 * numero2)
    elif eleccion == 4 and numero2 !=0:
            print ("")
            print ("Resultado: ", numero1, "/", numero2, "=", numero1 / numero2)
    elif eleccion == 5:
            print ("")
            print ("Resultado: ", numero1,"=" , numero1**0.5 ,numero2, "=", numero2**0.5)
    elif eleccion == 6:
            print ("")
            print ("Resultado: ", numero1, "**", numero2, "=", numero1 ** numero2)
    elif eleccion == 7:
            numero1 = int(input("Introduzca el primer numero: "))
            numero2 = int(input("Introduzca el segundo numero: "))
    elif eleccion == 8:
            print ("Chao")
