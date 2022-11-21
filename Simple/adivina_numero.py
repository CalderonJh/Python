import random


def run():
    numero = random.randint(1, 50)
    intentos = 0
    opcion = int(input("Elije un numero entre 1 y 50: "))
    while opcion != numero and intentos < 2:
        intentos += 1
        if opcion < numero:
            print(f"Es mayor, te quedan { 3 - intentos } intentos")
        else:
            print(f"Es menor, te quedan { 3 - intentos } intentos ")
        opcion = int(input("Elije otro numero: "))

    if intentos < 2:
        print()
        print(f"En efecto, era {numero}")
    else:
        print()
        print("Perdiste, no hay nadie peor que tú")
        print(f'El numero era {numero}')


if __name__ == '__main__':
    run()