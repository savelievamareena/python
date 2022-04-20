# # 5
# # Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.

from random import *

A = [randint(0, 10) for _ in 'abcd']
print(A)

for i in range(len(A)):
    if A[i] % 2 == 1:
        print("Нечетное число есть.")
        break
    if i == len(A) - 1:
        print("Нечетных чисел нет.")
