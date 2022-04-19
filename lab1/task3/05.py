# 5
# Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом и записать эти суммы в новый список B

import random

n = int(input("Введите размер списка: "))
A = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)

print(A)
B = []

for i in range(n):
    if i % 2 == 0:
        x = A[i] + A[i + 1]
        B.append(x)

print(B)
