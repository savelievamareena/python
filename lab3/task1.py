# Функция сортировки вставками insert
from random import *

N = int(input("Введите размер списка: "))
A = [randint(-100, 100) for _ in range(N)]
print(A)

for i in range(1, len(A)):
    t = A[i]
    j = i
    for j in range(i, 0, -1):
        if A[j - 1] > t:
            A[j] = A[j - 1]
            j -= 1
        else:
            break
    A[j] = t

print(A)

# Функция шейкерной (коктейльной) сортировки shaker

B = [randint(-100, 100) for _ in range(N)]
print(B)

for i in range(0, int(N / 2)):
    for j in range(i, N - 1 - i):
        if B[j] > B[j + 1]:
            temp = B[j]
            B[j] = B[j + 1]
            B[j + 1] = temp
    for j in range(N - 2 - i, i, -1): #если до i+1 как в условии то самый первый элемент не отсортирован*, работает правильно когда range до i
        if B[j] < B[j - 1]:
            temp = B[j]
            B[j] = B[j - 1]
            B[j - 1] = temp

print(B)