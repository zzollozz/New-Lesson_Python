import random
import re

def task_one():
    len_list = int(input('Задайте длину списка: '))
    number_list = [random.randint(1, 100) for _ in range(len_list)]
    number_search = int(input("Укажите число которое искать в списке: "))
    if number_search in number_list:
        print(f"число {number_search} повторяется {number_list.count(number_search)} раз")
    else:
        print('такого числа нет')
        count = 1
        while True:
            if number_search + count in number_list:
                print(f"Максимально близкое ему по значению: {number_search + count} повторяется "
                      f"{number_list.count(number_search + count)} раз")
                break
            elif number_search - count in number_list:
                print(f"Максимально близкое ему по значению: {number_search - count} повторяется "
                      f"{number_list.count(number_search - count)} раз")
                break
            count += 1

def task_two(letter_us, letter_rus):
    word = input('Введите слово для оценки: ')
    result = 0

    if bool(re.search('[а-яА-Я]', word)):
        letter = letter_rus
    elif bool(re.search('[a-zA-Z]', word)):
        letter = letter_us

    for k, v in letter.items():
        for el in list(map(str, word)):
            if el.upper() in list(map(lambda x: x.strip(), v.split(','))):
                result += k

    print(f'Стоимость слова "{word}" составляет {result} очков!')


def main():
    # Первая задача:
    # Задаем длину списка наполненного рандомными числами от 1 до 100.
    # Вводим искомое число X
    # Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
    # которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
    print(f"{'*' * 20} Первая задача {'*' * 20}")
    task_one()

    # Вторая задача:
    # В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
    # В случае с английским алфавитом очки распределяются так:
    letter_us = {
        1: 'A, E, I, O, U, L, N, S, T, R',
        2: 'D, G',
        3: 'B, C, M, P',
        4: 'F, H, V, W, Y',
        5: 'K',
        8: 'J, X',
        10: 'Q, Z'
    }
    # А русские буквы оцениваются так:
    letter_rus = {
        1: 'А, В, Е, И, Н, О, Р, С, Т',
        2: 'Д, К, Л, М, П, У',
        3: 'Б, Г, Ё, Ь, Я',
        4: 'Й, Ы',
        5: 'Ж, З, Х, Ц, Ч',
        8: 'Ш, Э, Ю',
        10: 'Ф, Щ, Ъ'
    }
    # Напишите программу, которая вычисляет стоимость введенного пользователем слова.
    # Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
    # Например: ноутбук - 12
    print(f"{'*' * 20} Вторая задача {'*' * 20}")
    task_two(letter_us, letter_rus)



if __name__ == '__main__':
    main()
