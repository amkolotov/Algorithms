# coding=utf-8
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1Nfb_wTIPfVEJhZHD4U9yK8qHiUtVhNwH/view?usp=sharing

print('Введите два числа и знак операции, введение нуля в качестве знака операции завершит программу.')

while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    s = input('Введите знак операции: ')

    if s == '0':
        print('Завершение работы программы')
        break
    elif s == '+':
        print(f'a + b = {a + b}')
    elif s == '-':
        print(f'a - b = {a - b}')
    elif s == '*':
        print(f'a * b = {a * b}')
    elif s == '/':
        if b != 0:
            print(f'a / b = {a / b}')
        else:
            print('На ноль делить нельзя')
    else:
        print('Введен некорректный знак операции.')