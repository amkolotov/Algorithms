# -*- coding: utf-8 -*-

# отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечание: - алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных.
# Постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировок, например, расчесткой, шейкерная и другие в зачет не идут.

import random

MIN_NUM = -100
MAX_NUM = 100
SIZE = 10

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]

print(array)

def bubble(arr):
    for i in range(len(arr) - 1):
        act = 0
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                act += 1
        if act == 0:
            break
    return arr
       
print(bubble(array))
        