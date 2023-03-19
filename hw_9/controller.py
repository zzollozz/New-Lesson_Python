import view
from model import PhoneBook


def start():
    while True:
        main_menu = view.main_menu()
        match main_menu:
            case 1:  # Открыть файл
                name_file = input('Укажите имя файла: ')
                phonebook = PhoneBook(name_file)
                view.print_result_fanc(phonebook.open_file(f'{name_file}.json'))
            case 2:  # Сохранить файл
                view.print_result_fanc(phonebook.save_file(name_file))
            case 3:  # Показать все записи
                try:
                    res = phonebook.read_contacts()
                    view.print_phonebook(res)
                except UnboundLocalError:
                    view.print_result_fanc('Выполните пункт 1')
            case 4:  # Создать контакт
                try:
                    view.print_result_fanc(phonebook.create_contact(view.input_update_data()))
                except UnboundLocalError:
                    view.print_result_fanc('Выполните пункт 1')
            case 5:  # Изменить контакт
                try:
                    id_cont = input('Укажите ID контакта: ')
                    view.print_result_fanc(phonebook.update_contact(id_cont, view.input_update_data()))
                except UnboundLocalError:
                    view.print_result_fanc('Выполните пункт 1')
            case 6:  # Найти контакт
                try:
                    patern = input("Укажите текст для поиска: ")
                    view.print_phonebook(phonebook.read_contacts(patern))
                except UnboundLocalError:
                    view.print_result_fanc('Выполните пункт 1')
            case 7:  # Удалить контакт
                try:
                    id_cont = input('Укажите ID контакта: ')
                    view.print_result_fanc(phonebook.delete_contact(id_cont))
                except UnboundLocalError:
                    view.print_result_fanc('Выполните пункт 1')
            case 8:
                break
