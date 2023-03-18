i = 0
while i < 15:
    print(i)
    i +=1
print("Ciclo terminado")

num = 0
while num < 20:
    num +=1
    if num%2 == 0:
        print(num)
        

num = 0
num2 = int(input("Ingrese el limite de rango"))
while num < num2:
    num +=1
    if num%2 == 0:
        print(num)
        
contraseña = input("Ingrese contraseña: ")
confcontraseña = input("Confirma contraseña: ")

if contraseña == confcontraseña:
    print("ingresa")
elif contraseña != confcontraseña:
    print("Solo tenias una oportunidad, pendejo")
    