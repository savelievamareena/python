# 7
# В переменную Y ввести номер года. Определить, является ли год високосным.

Y = int(input("Введите год: \n"))
if Y % 4 == 0:
    print("Год является високосным.")
else:
    print("Год не является високосным.")
