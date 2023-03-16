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
import re
from pprint import pprint


class PhoneBook:
    """
    Телефонная книга
    """
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

    def find_contact(self, firstName=None, surname=None, phone_number=None):
        id_list = []
        for id_key, cont in self.phonebook.items():
            if firstName != None:
                if cont.get('firstName') == firstName:
                    id_list.append(id_key)
            elif surname != None:
                if cont.get('surname') == surname:
                    id_list.append(id_key)
            elif phone_number != None:
                if cont.get('phone_number') == phone_number:
                    id_list.append(id_key)
        print()
        id_list = set(id_list)
        return id_list

    def create_contact(self, firstName, surname, phone_number):
        """
        Создание Контакта
        :param firstName:
        :param surname:
        :param phone_number:
        :return:
        """
        id_key = len(self.phonebook.keys())
        if self.phonebook.get(str(id_key)):
            while self.phonebook.get(str(id_key)):
                id_key += 1
        if ' ' in re.findall(r'[,;:+ -]', phone_number):
            phone_number = list(map(lambda x: int(x.strip()), phone_number.split(re.findall(r'[,;:+ -]', phone_number)[0])))

        contact = self.read_contacts(firstName, surname, phone_number)

        if contact != None:
            if contact.get('firstName') == firstName and contact.get('surname') == surname and contact.get('phone_number') == phone_number:
                 return f"контакт с таким именем {firstName} и фамилией {surname} и номером телефона есть"

        else:
            self.phonebook[id_key] = {'firstName': firstName,
                                      'surname': surname,
                                      'phone_number': phone_number
                                      }
            print(f'контакт id {id_key}: {firstName}  добавлен')

            return self.save_file(self.name_file, self.phonebook)

    def update_contact(self, id_contact, new_firstName=None, new_surname=None, new_phone_number=None):
        """
        Обновление контакта
        :param id_contact:
        :param new_firstName:
        :param new_surname:
        :param new_phone_number:
        :return:
        """
        contact = self.phonebook.get(id_contact)

        firstName = new_firstName if new_firstName != None else contact.get('firstName')
        surname = new_surname if new_surname != None else contact.get('surname')
        phone_number = new_phone_number if new_phone_number != None else contact.get('phone_number')

        update_contact = {'firstName': firstName,
                          'surname': surname,
                          'phone_number': phone_number
                          }
        self.phonebook[id_contact] = update_contact
        print(f'Контакт id: {id_contact} {firstName} {surname} обновлен ')
        return self.save_file(self.name_file, self.phonebook)

    def read_contacts(self, new_firstName=None, new_surname=None, new_phone_number=None):
        """
        Вывод всех контактов Телефоннй Книги
        или
        :param get_id: -> поиск по ID контакта
        :return:
        """
        if new_firstName or new_surname or new_phone_number:
            id_list_cont = self.find_contact(new_firstName, new_surname, new_phone_number)
            if id_list_cont:
                for cont in id_list_cont:
                    print(f'Имя: {self.phonebook.get(str(cont)).get("firstName")}, Фамилия: {self.phonebook.get(str(cont)).get("surname")}, Телефон: {self.phonebook.get(str(cont)).get("phone_number")}')
                    return self.phonebook.get(str(cont))
            else:
                return None
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



    #   Результат:


phonebook = PhoneBook('phonebook.json')  # объект класса с аргументом названия файла тел. книги

# pprint(phonebook.read_contacts('Smit')) # Вывод Нужного контакта
# pprint(phonebook.create_contact('Smit', 'Shhhhh', "79991112233, 453453453453"))  # Создание Нового контакта в телефонной книге
# pprint(phonebook.create_contact('Bob', 'Boby', "79991112233"))  # Создание Нового контакта в телефонной книге
# pprint(phonebook.create_contact('Tom', 'Tomy', "74546456456747"))  # Создание Нового контакта в телефонной книге
# pprint(phonebook.read_contacts())  # Вывод всех контактов книги
# pprint(phonebook.delete_contact('2'))  # Удаление контакта в телефонной книге
pprint(phonebook.update_contact('3', None, 'UPDATE', '70000000000'))  # Обновление данных контакта в телефонной книге
