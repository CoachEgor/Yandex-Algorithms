# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:02:31 2021

@author: Овчинниковы
"""
import time


# Телефонные номера в адресной книге мобильного телефона имеют один из следующих 
# форматов: +7<код><номер> 8<код><номер> <номер> где <номер> — это семь цифр, а 
# <код> — это три цифры или три цифры в круглых скобках. Если код не указан, то 
# считается, что он равен 495. Кроме того, в записи телефонного номера может стоять 
# знак “-” между любыми двумя цифрами (см. пример). На данный момент в адресной 
# книге телефона Васи записано всего три телефонных номера, и он хочет записать 
# туда еще один. Но он не может понять, не записан ли уже такой номер в телефонной 
# книге. Помогите ему! Два телефонных номера совпадают, если у них равны коды и 
# равны номера. Например, +7(916)0123456 и 89160123456 — это один и тот же номер.

# Формат ввода
# В первой строке входных данных записан номер телефона, который Вася хочет 
# добавить в адресную книгу своего телефона. В следующих трех строках записаны 
# три номера телефонов, которые уже находятся в адресной книге телефона Васи. 
# Гарантируется, что каждая из записей соответствует одному из трех приведенных 
# в условии форматов.

# Формат вывода
# Для каждого телефонного номера в адресной книге выведите YES (заглавными 
# буквами), если он совпадает с тем телефонным номером, который Вася хочет 
# добавить в адресную книгу или NO (заглавными буквами) в противном случае.



test_1 = ['8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', '8-495-430']

test_2 = ['86406361642', '83341994118', '86406361642', '83341994118']

test_3 = ['+78047952807', '+78047952807', '+76147514928', '88047952807']


start_time = time.time()


def is_exist_phone_number(x):
    new_phone_num = x[0].replace('(', '').replace(')', '').replace('-', '').replace('+7','8')
    exists_phones_nums = x[1:]
    
    for i, _ in enumerate(exists_phones_nums):
        exists_phones_nums[i] = exists_phones_nums[i].replace('(', '').replace(')', '').replace('-', '').replace('+7','8')
        
    for number in exists_phones_nums:
        if new_phone_num == number:
            print('YES')
        else:
            print('NO')


    return 'End'


print(is_exist_phone_number(test_1))
print(is_exist_phone_number(test_2))
print(is_exist_phone_number(test_3))

print("Время %s секунд" % (time.time() - start_time))