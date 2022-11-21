def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    p_invertida = palabra[::-1]
    if palabra == p_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_pld = palindromo(palabra)
    if es_pld:
        print("Es palindromo")
    else:
        print("No es palimdromo")


if __name__ == '__main__':
    run()
