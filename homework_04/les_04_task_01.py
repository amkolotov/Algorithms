# coding=utf-8
# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile


def rec_func(n):
    if n == 1:
        return 1
    else:
        return 1 / (- 2) ** (n -1) + rec_func(n - 1)

# print(rec_func(10))

print(timeit.timeit('rec_func(10)', number=1000, globals=globals()))   # 0.00803509999999999
print(timeit.timeit('rec_func(100)', number=1000, globals=globals()))  # 0.16195229999999997
print(timeit.timeit('rec_func(500)', number=1000, globals=globals()))  # 1.3545303

cProfile.run('rec_func(10)')
#  10/1    0.000    0.000    0.000    0.000 les_04_task_01.py:17(rec_func)
cProfile.run('rec_func(100)')
# 100/1    0.000    0.000    0.000    0.000 les_04_task_01.py:17(rec_func)
cProfile.run('rec_func(500)')
# 500/1    0.002    0.000    0.002    0.002 les_04_task_01.py:17(rec_func)

def sum_func(n):
    sum_ = 1
    a = 1
    for i in range(1, n):
        a /= -2
        sum_ += a
    return sum_

# print(sum_func(10))

print(timeit.timeit('sum_func(10)', number=1000, globals=globals()))   # 0.0017556999999999157
print(timeit.timeit('sum_func(100)', number=1000, globals=globals()))  # 0.014019499999999852
print(timeit.timeit('sum_func(500)', number=1000, globals=globals()))  # 0.07377560000000005

cProfile.run('sum_func(10)')
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:36(sum_func)
cProfile.run('sum_func(100)')
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:36(sum_func)
cProfile.run('sum_func(500)')
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:36(sum_func)

def arr_func(n):
    arr = [1 / (-2) ** i for i in range(1, n)]
    sum_ = 1
    for i in arr:
        sum_ += i
    return sum_

# print(arr_func(10))

print(timeit.timeit('arr_func(10)', number=1000, globals=globals()))   # 0.004571700000000067
print(timeit.timeit('arr_func(100)', number=1000, globals=globals()))  # 0.11740720000000016
print(timeit.timeit('arr_func(500)', number=1000, globals=globals()))  # 1.1000705

cProfile.run('arr_func(10)')
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:57(arr_func)
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:58(<listcomp>)
cProfile.run('arr_func(100)')
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:57(arr_func)
#  1    0.000    0.000    0.000    0.000 les_04_task_01.py:58(<listcomp>)
cProfile.run('arr_func(500)')
#  1    0.000    0.000    0.001    0.001 les_04_task_01.py:57(arr_func)
#  1    0.001    0.001    0.001    0.001 les_04_task_01.py:58(<listcomp>)

# По результатам замеров 3 вариантов функций для N равных 10, 100 и 500 можно сделать вывод, что самая эффективная
# реалицация алгоритма по скорости и сложности выполнение функция №2 с помощью использования одного цикла for.
# В первой функции испоьзуется рекурсия, вследствие чего образуется стек вызова функций, в третьей функции затрачиваются
# дополнительные ресурсы и память на создание массива с помощью генератора списков.