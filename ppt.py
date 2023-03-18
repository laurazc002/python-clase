usuario_opcion = input("Piedra, Papel o Tijera = ")
computador_opcion = "Tijera"

if usuario_opcion == computador_opcion : print("Empate")
elif usuario_opcion == "Piedra":
  if computador_opcion == "Tijera":
    print("Piedra gana a Tijera")
    print("Ganaste")
  else:
    print("Papel gana a Piedra")
    print("Computador ganó")
elif usuario_opcion == "Papel":
  if computador_opcion == "Piedra":
    print("Papel gana a Tijera")
    print("Ganaste")
  else:
    print("Tijera gana a Papel")
    print("Computador ganó")
elif usuario_opcion == "Tijera":
  if computador_opcion == "Papel":
    print("Tjera gana a Papel")
    print("Ganaste")
else:
  print("Piedra gana a Tijera")
  print("Computador ganó")