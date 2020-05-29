# coding=utf-8
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
# [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def sum_hex(inp_deq):
    first = inp_deq.pop()
    for _ in range(len(inp_deq)):
        second = inp_deq.pop()
        mind = 0
        count = deque()
        if len(first) < len(second):
            first, second = second, first
        for _ in range(len(first)):
            if second:
                res = TO_INT[first.pop()] + TO_INT[second.pop()] + mind
            else:
                res = TO_INT[first.pop()] + mind
            mind = res // 16
            res %= 16
            count.appendleft(TO_HEX[res])
        if mind == 1:
            count.appendleft(TO_HEX[mind])
        first = count
    return first


def mult_hex(inp_deq):
    first = inp_deq.pop()
    for _ in range(len(inp_deq)):
        second = inp_deq.pop()
        mult_deq = deque()
        if len(first) < len(second):
            first, second = second, first
        for i in range(len(second)):
            sum_deq = deque()
            if i > 0:
                [sum_deq.append('0') for _ in range(i)]
            mind = 0
            mult = TO_INT[second.pop()]
            for j in range(len(first)):
                res = TO_INT[first[-1-j]] * mult + mind
                mind = res // 16
                res %= 16
                sum_deq.appendleft(TO_HEX[res])
            if mind > 0:
                sum_deq.appendleft(TO_HEX[mind])
            mult_deq.appendleft(deque(sum_deq))

        first = sum_hex(mult_deq)

    return first


TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
      'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
TO_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
       10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

a = deque()
print('Ведите числа в шестнадцатеричном формате, для окончании ввода введите знак операции "+" или "*"')
while True:
    n = (input('Введите число: '))

    if n == '+':
        print(f'Сумма чисел равна {list(sum_hex(a))}')
        break
    elif n == '*':
        print(f'Произведение чисел равно {mult_hex(a)}')
        break
    else:
        a.append(deque(n))

