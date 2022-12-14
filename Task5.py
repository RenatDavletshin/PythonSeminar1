# Напиште программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15 но не 30

user_number = int(input('Enter your number: '))
if(user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number != 30:
    print('Your name is nice!')
else:
    print('Try again.')