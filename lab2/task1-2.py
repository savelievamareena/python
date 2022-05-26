# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
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

print(f"Максимальное нечетное число: {max(odds)}")
print(f"Минимальное число по модулю: {min(mod)}")

# решение через фильтр и мапу


def odds_fun(num):
    return True if num % 2 == 1 else False


def mod_fun(num):
    return abs(num)


A = [randint(-1000, 1000) for _ in range(20)]
print(A)

odds = list(filter(odds_fun, A))
mod = list(map(mod_fun, A))

print(f"Максимальное нечетное число: {max(odds)}")
print(f"Минимальное число по модулю: {min(mod)}")
