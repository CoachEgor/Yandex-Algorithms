# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:54:37 2021

@author: Овчинниковы
"""

# Решите в целых числах уравнение:

# sqrt(ax + b)=c

# a, b, c – данные целые числа: найдите все решения или сообщите, что решений 
# в целых числах нет.

# Формат ввода
# Вводятся три числа a, b и c по одному в строке.

# Формат вывода
# Программа должна вывести все решения уравнения в порядке возрастания, либо 
# NO SOLUTION (заглавными буквами), если решений нет.

temp_1 = [1, 0, 0]
temp_2 = [1, 2, 3]
temp_3 = [1, 2, -3]


def solution(x):
    a = x[0]
    b = x[1]
    c = x[2]
    
    if a >=0 and b >=0 and c>= 0:
        return int((c**2 / a) - (b / a))
    else:
        return 'NO SOLUTION'


print(solution(temp_1))
print(solution(temp_2))
print(solution(temp_3))