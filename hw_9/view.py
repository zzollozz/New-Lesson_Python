import file_message


def print_message_boundary(fanc):
    def wrapper(*args, **kwargs):
        print('*' * len(*args))
        f = fanc(*args, **kwargs)
        print('*' * len(*args))
        return f

    return wrapper


def main_menu():
    print(file_message.main_menu)
    select_menu = input('Выбирите пункт меню: ')
    len_select_menu = len(file_message.main_menu.split('\n')) - 1

    if select_menu.isdigit() and 0 < int(select_menu) <= len_select_menu:
        return int(select_menu)
    else:
        print(f'Введите число от 1 до {len_select_menu}')


@print_message_boundary
def print_result_fanc(message):
    print(message)


@print_message_boundary
def print_phonebook(obj: dict):
    for key, val in obj.items():
        print(
            f'| id: {key}, | Имя: {val.get("firstName"):<15} | Фамилия: {val.get("surname"):<15} | Ном.телефона: {val.get("phone_number")}')


def input_update_data():
    print("Укажите новые данные")
    firstName = input('Введите Имя: ')
    firstName = firstName if firstName != '' else None
    surname = input('Введите Фамилию: ')
    surname = surname if surname != '' else None
    phone_number = input('Введите номер или номера телефона: ')
    phone_number = phone_number if phone_number != '' else None
    return firstName, surname, phone_number
