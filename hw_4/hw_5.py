# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def recursive_exponentiation(num, power):
    if power == 0:
        return 1
    elif power == 1:
        return num
    elif power != 1:
        return num * recursive_exponentiation(num, power - 1)


numbers = int(input('Введите число: '))
power = int(input('Укажите в какую степень возвести: '))
print(f'{numbers} ˆ {power} = {recursive_exponentiation(numbers, power)}')


# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def recursive_sum(number_one, number_two):
    if number_two == 0:
        return number_one
    else:
        return recursive_sum(number_one + 1, number_two - 1)


number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
print(f'{number_one} + {number_two} = {recursive_sum(number_one, number_two)}')
