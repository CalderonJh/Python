import numpy as np
import time

arr = np.array([9, -1, 3, 2, -1, 10, 5, 6, -12, 0, 9])
print(str(arr))

tim_ini = time.time()
for i in range(arr.size - 1):
    minimum = i  # = 1
    for j in range(i + 1, arr.size):  # 4 -> 1
        if arr[j] < arr[minimum]:
            minimum = j
    arr[i], arr[minimum] = arr[minimum], arr[i]


tim_fin = time.time()
tim_total = tim_fin - tim_ini

print(str(arr))
print("Tiempo: ", tim_total)
