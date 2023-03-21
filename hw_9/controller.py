import view
from model import PhoneBook


def start():
    name_file = input('Укажите имя файла: ')
    phonebook = PhoneBook(name_file)

    while True:
        if isinstance(phonebook.phonebook, str):
            view.print_result_fanc(phonebook.phonebook)
            start()
        main_menu = view.main_menu()

        match main_menu:
            case 1:  # Показать все записи
                view.print_phonebook(phonebook.read_contacts())
            case 2:  # Создать контакт
                view.print_result_fanc(phonebook.create_contact(view.input_update_data()))
            case 3:  # Изменить контакт
                id_cont = input('Режим Изменения <--\nУкажите ID контакта: ')
                view.print_result_fanc(phonebook.update_contact(id_cont, view.input_update_data()))
            case 4:  # Найти контакт
                patern = input("Режим Поиска <--\nУкажите текст для поиска:  ")
                view.print_phonebook(phonebook.read_contacts(patern))
            case 5:  # Удалить контакт
                id_cont = input('Режим Удаления <--\nУкажите ID контакта: ')
                view.print_result_fanc(phonebook.delete_contact(id_cont))
            case 6:
                break
