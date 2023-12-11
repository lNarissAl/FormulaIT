money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

current_month = 0
budget = money_capital + salary  # общий бюджет

while True:
    monthly_spend = spend * (1 + increase) ** current_month  # траты в месяц
    budget += salary - monthly_spend  # остаток на месяц
    current_month += 1
    money_capital = budget  # меняем остаток подушки на следующий месяц

    if monthly_spend > budget:  # прерываем цикл, когда траты превышают остаток
        break

print("Количество месяцев, которое можно протянуть без долгов:", current_month)
