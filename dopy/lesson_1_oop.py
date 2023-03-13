"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time
from turtle import title


class TrafficLight:
    _color = [('красный', 7), ('желтый', 2), ('зеленый', 5)]

    def running(self):
        i = 0
        while True:
            if i == 3:
                i = 0
            print(f'\r{self._color[i][0]}', end=' ')
            time.sleep(self._color[i][1])
            i += 1


# a = TrafficLight()
# a.running()


"""
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т

"""


class Road:

    def __init__(self, length, width, mass_of_asphalt, tolchina_polotna):
        self._length = length
        self._width = width
        self.mass_of_asphalt = mass_of_asphalt
        self.tolchina_polotna = tolchina_polotna

    def asphalt_mass_calculation_method(self):
        res = self._length * self._width * self.mass_of_asphalt * self.tolchina_polotna / 1000
        return f"{self._length}м * {self._width}м * {self.mass_of_asphalt}кг * {self.tolchina_polotna}см = {int(res)} т"


#  Результат работы:

a = Road(20, 5000, 25, 5)
print(a.asphalt_mass_calculation_method())

"""
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);

● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:  # Работник

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus}


class Position(Worker):  # Должность

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):  # дохода с учётом премии
        return f'{self._income.get("wage") * self._income.get("bonus")}'


#  Результат работы:

# id_user = Position('Tom', 'Tramp', 'Президенит', 20, 7)
#
# print(f'Имя сотрудника: = {id_user.get_full_name()}')
# print(f'Должность: = {id_user.position}')
# print(f'Сумма дохода с учетом премии = {id_user.get_total_income()} бобов')

"""
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

● Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    """ Автомобиль """

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        """
        автомобиль поехал
        :return:
        """
        return f'{self.name} Машина поехала'

    def stop(self):
        """
        автомобиль остановился
        :return:
        """
        return f'{self.name} машина остановилась'

    def turn(self, direction: str):
        """
        поворот (направление) автомобиля
        :return:
        """
        if direction.lower() == 'left':
            res = 'машина повернула на лево'
        elif direction.lower() == 'right':
            res = 'машина повернула на право'
        else:
            res = 'определись с направлением!'
        return res

    def show_speed(self):
        """
         текущую скорость автомобиля
        :return:
        """
        return f'текущаяя сколость: {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышении скорости!'
        else:
            return f'{self.name} скорость: {self.speed} км/ч'

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} превышении скорости!'
        else:
            return f'{self.name} скорость: {self.speed} км/ч'


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)



#  Результат работы:


# police_car = PoliceCar('ДПС', 'Белый', 80,)
# print(police_car.go())
# print(police_car.is_police)
# print(police_car.stop())

# print(police_car.turn('left'))
# print(police_car.turn('right'))


# town_car = TownCar('Reno', 'Grey', 30,)
# print(town_car.show_speed())
# print(town_car.is_police)
# print(town_car.name)
# print(town_car.color)

"""
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;

● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:
    """
    канцелярская принадлежность
    """
    def __init__(self, title):
        self.title = title

    def draw(self):
        """
        отрисовка
        :return:
        """
        return f'Запуск отрисовки'

class Pen(Stationery):
    """
    Ручка
    """
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        return f'Пишем {self.title} цвет {self.color}'

pen = Pen('ручка', 'черная')
print(pen.draw())

