# -*- coding: utf-8 -*-

# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque


class MyNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def go(self, code, n):
        self.left.go(code, n + '0')
        self.right.go(code, n + '1')


class MyLeaf:
    def __init__(self, value):
        self.value = value

    def go(self, code, n):
        code[self.value] =  n
        

def encode(string):
    if len(string) <= 1:
        print('Строка должна содержать больше одного символа.')
        return
    count_list = [(chr_count, MyLeaf(chr)) for chr, chr_count in Counter(string).items()]
    i = 1
    sort_list = deque()
    while len(count_list) != len(sort_list):
        for j in count_list:
            if j[0] == i:
                sort_list.append(j)
        i += 1
    
    while len(sort_list) > 1:
        count_1, chr_left = sort_list.popleft()
        count_2, chr_right = sort_list.popleft()
        num = count_1 + count_2

        if sort_list:
            for i in range(len(sort_list)):
                if sort_list[i][0] >= num:
                    sort_list.insert(i, (num, MyNode(chr_left, chr_right)))
                    break
                elif sort_list[i][0] != num and i == len(sort_list) - 1:
                    sort_list.append((num, MyNode(chr_left, chr_right)))
        else:
            sort_list.append((num, MyNode(chr_left, chr_right)))

    return sort_list[0][1]


def decode(code):
    decode_str = ''
    code_let = ''
    for i in range(len(code)):
        code_let += code[i]
        for chr, num in my_dict.items():
            if num == code_let:
                decode_str += chr
                code_let = ''
    return decode_str


while True:
    s = input('Введите текст для кодирования: ')
    if len(s) < 2:
        print('Строка не должна быть менее двух символов')
    else:
        my_dict = {}
        code = encode(s)
        code.go(my_dict, '')
        print(my_dict)

        res_code = ''
        for i in s:
            res_code += my_dict[i]

        print(res_code)
        print(f'Была закодрована строка: {decode(res_code)}')

        break