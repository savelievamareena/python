# 11
# Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
from random import *
import numpy as np

arr = [randint(0, 10) for _ in 'abc']
print(arr)

d = max(arr)
print(f"Самое большое число: {d}")
