# сортировка
from random import *

N = int(input("Введите размер списка: "))
A = [randint(-100, 100) for _ in range(N)]
print(A)

for i in range(1, len(A)):
    t = A[i]
    j = i
    for j in range(i, 0, -1):
        if A[j-1] > t:
            A[j] = A[j-1]
            j -= 1
        else:
            break
    A[j] = t

print(A)
