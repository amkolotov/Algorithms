# -*- coding: utf-8 -*-

# массив размером 2m + 1, где m - натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элемены, которые не
# меньше медианы, в другой - не больше медианы.

from random import randint

MIN_NUM = 0
MAX_NUM = 100
m = int(input('Введите коэффициент m: '))

array = [randint(MIN_NUM, MAX_NUM) for _ in range(2 * m + 1)]

print(array)

for i in range(len(array)):
    les_count = 0
    great_count = 0
    for j in range(len(array)):
        if array[j] <= array[i]:
            les_count += 1
        if array[j] >= array[i]:
            great_count += 1
    if les_count > m and great_count > m:
        break
print(f'Медианой в массиве является число {array[i]}')

            
            
            
            
            
            
            
            