# coding=utf-8
# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import math
import timeit
import cProfile


def sieve(n):
    if n == 1:
        max_num = 3
    else:
        max_num = n * 2 * round(math.log(n))
    sieve = [i for i in range(max_num)]
    sieve[1] = 0
    for i in range(2, max_num):
        if sieve[i] != 0:
            j = i + i
            while j < max_num:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[n-1]

# print(sieve(1000))

print(timeit.timeit('sieve(10)', number=1000, globals=globals()))   # 0.022077
print(timeit.timeit('sieve(100)', number=1000, globals=globals()))  # 0.6041645
print(timeit.timeit('sieve(1000)', number=1000, globals=globals())) # 9.007404600000001

cProfile.run('sieve(10)')
# 1    0.000    0.000    0.000    0.000 les_04_task_02.py:17(sieve)
# 1    0.000    0.000    0.000    0.000 les_04_task_02.py:22(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_04_task_02.py:30(<listcomp>)
cProfile.run('sieve(100)')
# 1    0.001    0.001    0.001    0.001 les_04_task_02.py:17(sieve)
# 1    0.000    0.000    0.000    0.000 les_04_task_02.py:22(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_04_task_02.py:30(<listcomp>)
cProfile.run('sieve(1000)')
# 1    0.014    0.014    0.023    0.023 les_04_task_02.py:17(sieve)
# 1    0.007    0.007    0.007    0.007 les_04_task_02.py:22(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_04_task_02.py:30(<listcomp>)

def prime(n):
    n_prime = 0
    i = 1
    while n_prime < n:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            n_prime += 1
    return i

# print(prime(5))

print(timeit.timeit('prime(10)', number=1000, globals=globals()))   # 0.025250200000000333
print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # 2.3743280999999996
print(timeit.timeit('prime(1000)', number=1000, globals=globals())) # 602.4920289

cProfile.run('prime(10)')
# 1    0.000    0.000    0.000    0.000 les_04_task_02.py:46(prime)
cProfile.run('prime(100)')
# 1    0.007    0.007    0.007    0.007 les_04_task_02.py:46(prime)
cProfile.run('prime(1000)')
# 1    0.489    0.489    0.489    0.489 les_04_task_02.py:46(prime)