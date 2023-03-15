# Задача 34:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам
import re


def winnie_pooh_counts(poem: str):
    """
    Вычисление ритма стихотворения
    :param poem:
    :return str:
    """
    glas = 0
    soglas = 0
    try:
        list_fraz = [len(re.findall(r'[ауоыиэяюёе]', i)) for i in poem.split(' ')]
        patern = list_fraz[0]
        if len(list_fraz) < 2:
            raise Exception('Одна фраза думай еще!')
        for fraza in list_fraz:
            if fraza == patern:
                glas += 1
            else:
                soglas += 1
        return f'Пам парам' if soglas != 0 else 'Парам пам-пам'
    except Exception as ex:
        return ex

    # Проверка

# data = 'пара-ра-рам'
# data = 'пара-ра-рам рам-пам-папам па-р-па-да'
# data = 'пара-ра-рам рам-бпам па-ра-па-да'
# data = 'пара-ра-рам рам-пм-папам па-ра-па-да'
data = 'пара-ра-рам рам-пам-папам па-ра-па-да'  # Trye

print(winnie_pooh_counts(data))



# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def element_row_and_column_number(fanc): # вычисляющую элемент по номеру строки и столбца
    return fanc


def print_operation_table(operation, num_rows=6, num_columns=6):
    list = []
    for i in range(1, num_rows + 1):
        list.append([])
        for j in range(1, num_columns + 1):
            list[i-1].append(operation(i, j))
            # list[i-1].append(element_row_and_column_number(operation(i, j)))
    return '\n'.join(map(str, list))

    # проверка
# print(print_operation_table(lambda x, y: x * y))
print(print_operation_table(lambda x, y: x * y, 10, 9))
