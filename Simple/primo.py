def es_primo(numero):
    for i in range( 2, numero):
        if numero % i == 0:
            return False
    return True    


def run():
    numero = int(input("Dijite un numero: "))
    if numero > 1:
        if es_primo(numero):
            print("Es primo")
        else:
            print("No es primo")
    else:
        print("Dijite un numero mayor que 1")
  

if  __name__ == '__main__':
    run()