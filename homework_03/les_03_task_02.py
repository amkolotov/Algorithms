# coding=utf-8
# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

ind_array = []

for i, item in enumerate(array):
    if item % 2 == 0:
        ind_array.append(i)

print(array)
print(ind_array)