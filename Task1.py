#  Напишите программу, которая принимает на вход два числа и проверяет, 
#  является ли одно число квадратом другого.
#  Например:
#  5, 25 -> да
#  4, 16 -> да
#  25, 5 -> да
#  8, 9 -> нет

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'{num1}, {num2} -> ', end=' ')
if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('да')
else:
    print('нет')