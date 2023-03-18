print("""
        Escoja el lenguaje de programacion :
        1. HTML
        2. CSS
        3. JAVASCRIPT
        4. PYTHON
        5. Salir 
          """)
eleccion = int(input(""))

while eleccion != 5:
    if eleccion == 1:
        print("HTML Sirve para estructura")
    elif eleccion == 2:
        print("CSS Sirve para diseño")
    elif eleccion == 3:
        print ("JAVASCRIPT Sirve para programar en javascript")
    elif eleccion == 4:
        print ("PYTHON Sirve para programar en Python")
    elif eleccion == 5:
        print ("salgase pues mijo")
    eleccion = int(input(""))
    