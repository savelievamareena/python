# 9
# Проверить, является ли дробь A / B правильной.

from random import *

a, b = [randint(0, 10) for _ in 'ab']
print(a, b)
if a/b < 1:
    print("Дробь правильная")
else:
    print("Дробь неправильная")