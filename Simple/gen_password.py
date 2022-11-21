import random

def run():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K',
    'L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','ñ','o','p','q','r','s','t','v','w','x','y','z']
    simbolos = ['!','#','$','%','.','/','?',',','-','_']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []

    for i in range(15):
        ran_car = random.choice(caracteres)
        password.append(ran_car)
    password = ''.join(password)
    
    print(f"Your password is {password}")


if __name__ == '__main__':
    run()