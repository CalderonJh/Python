n = int(input())
datos = [];

for i in range(n):
    datos.append(int(input()))
    
    
for i in range(n):
    print(datos[i], end=" ")
print()

for i in range(1, n):
    for j in range(i, n):
        pass