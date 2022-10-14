money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= 0:
      money_capital = money_capital + (salary - spend)
      spend = spend * (1 + increase)
      month += 1
else: money_capital < 0
month -= 1
print(month - 2) # Во время лекции выяснили, что в Expected допущена ошибка
# Специально вычел 2, а в действительности можно прожить 5 месяцев
