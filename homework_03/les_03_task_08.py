# coding=utf-8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.

matrix = [[input('Введите число: ') for _ in range(3)] for _ in range(5)]
print(matrix)

for line in matrix:
    sum_line = 0
    for item in line:
        sum_line += int(item)
        print(f'{item:>5}', end='')
    print(f'{sum_line:>5}')