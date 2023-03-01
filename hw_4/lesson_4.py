# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random

# 1 - создает список из рандомных четырех значных чисел
numbers_list = [random.randint(1000, 10000) for _ in range(10)]

print(numbers_list)

# 2 - принимает с консоли цифру и удаляет ее из всех элементов списка
number_user = int(input("введите число: "))
for index, val in enumerate(numbers_list):
    if str(val).find(str(number_user)) != -1:
        numbers_list[index] = (int(str(val).replace(str(number_user), '')))

print(numbers_list)

def sum_numbers(numbers_list):
    """
    Суммирует цифры каждого элемента пока результат не станет однозначным числом
    :param numbers_list:
    :return:
    """
    for index, val in enumerate(numbers_list):
        temp = sum(list(map(lambda x: int(x), ''.join(str(val)))))
        numbers_list[index] = temp
        if len(str(temp)) > 1:
            return sum_numbers(numbers_list)
    return numbers_list

# 3 - цифры каждого элемента суммирует пока результат не станет однозначным числом
print(sum_numbers(numbers_list))

# 4 - из финального списка убирает все дублирующиеся элементы
numbers_list = [value for ind, value in enumerate(numbers_list) if value not in numbers_list[:ind]]
print(numbers_list)






