# coding=utf-8
# Определить, какое число в массиве встречается чаще всего.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

uniq_array = list(set(array))
count, item = 0, 0

for i in uniq_array:
    n = 0
    for j in array:
        if i == j:
            n += 1
    if n > count:
        count = n
        item = i
print(item)