# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
import json
import os
from pprint import pprint


class PhoneBook:
    path = os.getcwd()

    def __init__(self, name_file):
        self.name_file = name_file
        self.phonebook = self.open_file(self.name_file)

    def open_file(self, name_file):
        try:
            with open(f'{self.path}/{name_file}') as file:
                return json.load(file)
        except Exception as ex:
            return 'Данный файл или каталог отсутствует'

    def save_file(self, name_file, data_for_save):
        with open(f'{self.path}/{name_file}', 'w') as file:
            json.dump(data_for_save, file, indent=4)
            return f'файл {name_file} обновлен'

    def create_contact(self, firstName, surname, phone_number):
        """
        Создание Контакта
        :param firstName:
        :param surname:
        :param phone_number:
        :return:
        """
        self.phonebook[str(len(self.phonebook.keys()))] = {'firstName': firstName,
                                                           'surname': surname,
                                                           'phone_number': [phone_number]
                                                           }
        print(f'контакт id {len(self.phonebook.keys())}: {firstName}  добавлен')
        return self.save_file(self.name_file, self.phonebook)

    def update_contact(self, id_contact, firstName=None, surname=None, phone_number=None):

        name_file = "sdsd"
        update_contact = {'firstName': firstName,
                    'surname': surname,
                    'phone_number': [phone_number]
                    }
        self.phonebook[id_contact] = update_contact
        return self.save_file(self, name_file, self.phonebook)

    def read_contacts(self, get_id=None):
        """
        Вывод всех контактов Телефоннй Книги
        или
        :param get_id: -> поиск по ID контакта
        :return:
        """
        if get_id:
            return self.phonebook.get(get_id)
        else:
            return self.phonebook

    def delete_contact(self, id_contact):
        """
        Удаление контакта
        :param id_contact:
        :return:
        """
        if not self.phonebook.get(id_contact):
            return f'Контакта с id: {id_contact} нет'
        else:
            print(f'контакт id {id_contact}: {self.phonebook.get(id_contact).get("firstName")} удален')
            del self.phonebook[id_contact]
            return self.save_file(self.name_file, self.phonebook)

    def find_contact(self, id_contact):
        id_contact = id_contact
        contact = self.phonebook.get(id_contact)
        return

    #   Результат:


phonebook = PhoneBook('phonebook.json')

# pprint(phonebook.read_contacts('1')) # Вывод Нучного контакта
# pprint(phonebook.create_contact('Smit', 'Shhhhh', '77772341178')) # Создание Нового контакта
# pprint(phonebook.read_contacts()) # Вывод всех контактов книги
pprint(phonebook.delete_contact('5')) # Удаление
pprint(phonebook.update_contact('6', '70009991188')) # Удаление
