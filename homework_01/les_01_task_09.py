# coding=utf-8
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if c > a:
        print(a)
    else:
        if c > b:
            print(c)
        else:
            print(b)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)
