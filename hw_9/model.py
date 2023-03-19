import json
import os
import re


class PhoneBook:
    """
    Телефонная книга
    """
    path = os.getcwd()

    def __init__(self, name_file):
        self.name_file = name_file
        self.phonebook = {}

    def open_file(self, name_file):
        try:
            with open(f'{self.path}/{name_file}') as file:
                self.phonebook = json.load(file)
                return f'Файл загружен!'
        except Exception as ex:
            return f'Данный файл или каталог отсутствует'

    def save_file(self, name_file):
        with open(f'{self.path}/{name_file}.json', 'w') as file:
            json.dump(self.phonebook, file, indent=4)
            return f'файл {name_file} записан!'

    def processing_phone_number(self, phone_number):
        if phone_number != None and ' ' in re.findall(r'[,;:+ -]', phone_number):
            return list(
                map(lambda x: int(x.strip()), phone_number.split(re.findall(r'[,;:+ -]', phone_number)[0])))
        else:
            return [int(phone_number) if phone_number != None else '']

    def find_contact(self, patern=None):
        id_list = []
        if patern != None:
            for id_key, cont in self.phonebook.items():
                if re.findall(str(patern).lower(), str(list(cont.values())).lower()):
                    id_list.append(id_key)
        id_list = set(id_list)
        return id_list

    def create_contact(self, *args):
        """
        Создание Контакта
        :param firstName:
        :param surname:
        :param phone_number:
        :return:
        """
        id_key = len(self.phonebook.keys())
        firstName = list(*args)[0]
        surname = list(*args)[1]
        phone_number = list(*args)[2]

        if self.phonebook.get(str(id_key)):
            while self.phonebook.get(str(id_key)):
                id_key += 1

        phone_number = self.processing_phone_number(phone_number)

        self.phonebook[id_key] = {'firstName': firstName if firstName != None else '',
                                  'surname': surname if surname != None else '',
                                  'phone_number': phone_number
                                  }
        return f'контакт id {id_key}: {firstName}  добавлен'

    def update_contact(self, id_contact, *args):
        """
        Обновление контакта
        :param id_contact:
        :param new_firstName:
        :param new_surname:
        :param new_phone_number:
        :return:
        """
        contact = self.phonebook.get(id_contact)
        phone_number = self.processing_phone_number(list(*args)[2])

        firstName = list(*args)[0] if list(*args)[0] != None else contact.get('firstName')
        surname = list(*args)[1] if list(*args)[1] != None else contact.get('surname')
        phone_number = phone_number if phone_number else contact.get('phone_number')

        update_contact = {'firstName': firstName,
                          'surname': surname,
                          'phone_number': phone_number
                          }
        self.phonebook[id_contact] = update_contact
        return f'Контакт id: {id_contact} {firstName} {surname} обновлен '

    def read_contacts(self, patern=None):
        """
        Вывод всех контактов Телефоннй Книги
        или
        :param get_id: -> поиск по ID контакта
        :return:
        """
        if patern:
            id_list_conts = self.find_contact(patern)
            res_find = {}
            if id_list_conts:
                for cont in id_list_conts:
                    res_find[str(cont)] = self.phonebook.get(str(cont))
            return res_find
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
            mes = f'контакт id {id_contact}: {self.phonebook.get(id_contact).get("firstName")} удален'
            del self.phonebook[id_contact]
            return mes

