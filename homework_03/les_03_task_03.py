# coding=utf-8
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min, max = array[0], array[0]
i_min, i_max = 0, 0

for i, item in enumerate(array):
    if item < min:
        min = item
        i_min = i
    elif item > max:
        max = item
        i_max = i
array[i_min], array[i_max] = array[i_max], array[i_min]

print(array)


