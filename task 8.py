money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
money = 0

month = 0  # количество месяцев, которое можно прожить

while money_capital + salary > spend * month:
    month += 1
    spend = spend * (increase + 1)

    # TODO Оформить решение
print(month)
