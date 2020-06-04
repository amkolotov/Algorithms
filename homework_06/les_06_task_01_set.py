# coding=utf-8
# Определить, какое число в массиве встречается чаще всего.

from random import randint
import sys

def my_size(object):
    size = 0
    size += sys.getsizeof(object)
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(object, str):
            for item in object:
                size += sys.getsizeof(item)
    return size

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


uniq_array = set(array)
freq, n = 0, 0

for i in uniq_array:
    count = 0
    for j in array:
        if i == j:
            count += 1
    if count > freq:
        freq = count
        n = i
print(f'Число {n} встречается {freq} раз в массиве.')

my_dict = globals().copy()
size = 0

for key, value in my_dict.items():
    size += my_size(key)
    size += my_size(value)
print(size) # 3838  байта, Windows 10, x64, Python 3.7