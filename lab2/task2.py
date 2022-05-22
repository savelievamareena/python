#Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
#Найдите минимальный по модулю элемент списка.

from random import *

A = [randint(-1000, 1000) for _ in range(20)]
print(A)

odds = []
mod = []
for i in range(0, len(A) - 1):
    if A[i] % 2 == 1:
        odds.append(A[i])
    modul = A[i] if A[i] > 0 else A[i] * -1
    mod.append(modul)

print("-----")
print(odds)
print(mod)
print(f"Максимальное нечетное число: {max(odds)}")
print(f"Максимальное число по модулю: {max(mod)}")
