# -*- coding: utf-8 -*-

# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

def hash_func(word):
    hash_list = []
    for i in range(len(word)):
        for j in range(i, len(word)):
            if word[i:j+1] == word or word[i:j+1] == ' ':
                continue
            elif hash(word[i:j+1]) not in hash_list:
                hash_list.append(hash(word[i:j+1]))

    return len(hash_list)

print(hash_func('papa'))
print(hash_func('sova'))
