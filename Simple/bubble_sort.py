n = int(input())
datos = [];

for i in range(n):
    datos.append(int(input()))
    
    
for i in range(n):
    print(datos[i], end=" ")
print()

for i in range(n-1):
    cambio = False
    for j in range(0, n-i-1):
        if datos[j] > datos[j+1]: 
            datos[j], datos[j+1] = datos[j+1], datos[j]
            cambio = True

    if not cambio:
        break
        
        
for i in range(n):
    print(datos[i], end=" ")           
