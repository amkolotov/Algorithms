# coding=utf-8

# https://drive.google.com/file/d/1q-NsCK0afxm4-YlAZUtPDsqOICv1A5QQ/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

n = int(input('Введите трехзначное число: '))

a = n // 100
b = (n // 10) % 10
c = n % 10

s = a + b + c
m = a * b * c

print(f'Сумма цифр числа равна {s}')
print(f'Произведение цифр числа равно {m}')