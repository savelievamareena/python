# 3
# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.
from random import *

A = [randint(0, 10) for _ in 'abc']
print(A)

ifZero = False
geom = 0
ar = 0

for i in range(len(A)):
    if i == 0:
        geom = A[i]
    else:
        geom *= A[i]
    ar += A[i]
    if A[i] == 0:
        ifZero = True

if ifZero:
    print(ar)
else:
    print(geom)
