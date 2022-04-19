# 4
# По номеру месяца напечатать пору года.

monthNumber = int(input("Введите номер месяца: \n"))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
if monthNumber <= 12:
    print(months[monthNumber - 1])
else:
    print("В году 12 месяцев.")
