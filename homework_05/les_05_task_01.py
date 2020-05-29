# coding=utf-8
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import Counter

number = int(input('Введите количество предприятий: '))
count_profit = Counter()
for i in range(number):
    name = input('Введите наименование предприятия: ')
    count_profit[name] = 0
    for i in range(1, 5):
        profit = int(input(f'Введите прибыль за {i} квартал: '))
        count_profit[name] += profit
sum_profit = 0
for value in count_profit.values():
    sum_profit += value

print(f'Средняя прибыль равна {sum_profit // number}')

print('Убыточные предприятия: ')
[print(key) for key, value in count_profit.items() if value < sum_profit // number]
print('Прибыльные предприятия: ')
[print(key) for key, value in count_profit.items() if value > sum_profit // number]

