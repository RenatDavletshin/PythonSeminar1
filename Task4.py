# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# num = input('Enter number: ')
# if '.' in num:
#     index_num = num.find('.')+1
#     print(num[index_num])
# elif ',' in num:
#     index_num = num.find(',')+1
#     print(num[index_num])
# else:
#     print('No')

num = float(input('Введите число: '))
if num % 1 == 0:
    print('Нет')
else:
    num = int(num*10 % 10)
    print(num)
