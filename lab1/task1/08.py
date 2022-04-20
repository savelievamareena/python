# 8
# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?

from random import *

number = randint(1000, 9999)
print(number)

A = []
flag = True

for i in range(4):
    if int(str(number)[i]) in A:
        flag = False
        print("No")
        break
    else:
        A.append(int(str(number)[i]))
if flag:
    print("Yes")
