#3.Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме элементов, стоящих
# на том же месте в 1-й и 2-й таблицах.
from random import *

n = int(input('Размерность квадратной таблицы: '))

matrix1 = [[randrange(1, 11) for _ in range(n)] for _ in range(n)]
matrix2 = [[randrange(1, 11) for _ in range(n)] for _ in range(n)]
print(matrix1)
print(matrix2)
matrix3 = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print(matrix3)
print("---------")

#1.В матрице найти номер строки, сумма чисел в которой максимальна.

matrix0 = [[randrange(1, 11) for _ in range(n)] for _ in range(n)]
print(matrix0)

max_row_sum = 0
row_num = 0
for i in range(n):
    if sum(matrix0[i]) > max_row_sum:
        max_row_sum = sum(matrix0[i])
        row_num = i + 1

print(f"В строке под номером {row_num} сумма чисел максимальна и равняется {max_row_sum}")
