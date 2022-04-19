# 2
# Торговая фирма в первый день работы реализовала товаров на P тыс. руб., а затем ежедневно увеличивала выручку на 3%.
# Какой будет выручка фирмы в тот день, когда она впервые превысит заданное значение Q?
# Сколько дней придется торговать фирме для достижения этого результата?

P = int(input("Введите сумму P: \n"))
Q = int(input("Введите значение Q: \n"))

days = 0
while P < Q:
    P += P * 0.03
    days += 1

print(f"Выручка: {int(P)} т.р.")
print(f"Количество дней для достижения цели: {days}")
