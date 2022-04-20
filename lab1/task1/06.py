# 6
# Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?

from random import *

number = randint(100, 999)
print(number)

for i in range(3):
    if str(number)[i] == "0" or str(number)[i] == "9":
        print("Yes")
        break
