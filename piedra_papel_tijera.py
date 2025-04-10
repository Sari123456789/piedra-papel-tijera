import random
opciones = ["piedra", "papel", "tijera"]
contador1= 0
contador2= 0

while True:
    elegida = input("Juguemos. Elige entre piedra, papel o tijera: ").lower()
    if elegida not in opciones:
        print("Elige una opción válida")
    else: 
        correcta = random.choice(opciones)
        print(f"La computadora eligió: {correcta}")


        if elegida == correcta:
            print(f"Empate de {elegida} contra {correcta}")
        elif (elegida == "papel" and correcta == "piedra") or (elegida == "piedra" and correcta =="tijera") or (elegida == "tijera" and correcta == "papel"):
            print("Gana usuario a ordenador")
            print(f"Gana {elegida} contra {correcta}")
            contador1 = +1
        else:
            print("Gana ordenador a usuario")
            print(f"Gana {correcta} contra {elegida}")
            contador2= +1


    print(f"Usuario = {contador1}")
    print(f"Ordenador = {contador2}")

