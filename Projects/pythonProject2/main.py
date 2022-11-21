n = int(input())

serie = 1;
denominador = 3

for i in range(2, n + 1, 1):
    if i % 2 == 0:
        signo = -1
    else: 
        signo = 1;
    serie += signo * 1/denominador;
    denominador +=2

pi = 4 * serie;

print(pi)