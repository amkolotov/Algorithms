# -*- coding: utf-8 -*-

# отсортируйте по возрастанию методом слияния одномерный вещественный массив заданный случайными числами на промежутке
# [0-50). Выведите на экран исходный и отсортированный массивы

import random

MIN_NUM = 0
MAX_NUM = 50
SIZE = 10

array = [random.random() * 50 for _ in range(SIZE)]

print(array)

def merge_arr(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        left_arr = merge_arr(left_arr)
        right_arr = merge_arr(right_arr)
        return merge(left_arr, right_arr)
        
def merge(left_arr, right_arr):
    sort_arr = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sort_arr.append(left_arr[i])
            i += 1
        else:
            sort_arr.append(right_arr[j])
            j += 1
    if i == len(left_arr):
        sort_arr += right_arr[j:]
    else:
        sort_arr += left_arr[i:]
    return sort_arr
    
print(merge_arr(array))
    
    
    
    
    
    
    
    
    