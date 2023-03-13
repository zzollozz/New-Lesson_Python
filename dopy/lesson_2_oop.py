                # Перезагрузка

class Test:
    name = 'тестовый класс'

    def __str__(self):
        return f'{self.name}'

# ts = Test()
# print(ts)

class MyClass:

    def __setattr__(self, attr, value):
        if attr == "width":
            self.__dict__[attr] = value
            print(self.__dict__)
        else:
            print(f"Атрибут {attr} недопустим")


# mc = MyClass()
# mc.width = 40
# mc.height = 40
# mc.width = 10



                # Переопределение методов
class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя")
    def my_method(self):
        print("Метод my_method() класса ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        print("Конструктор дочернего класса")
        ParentClass.__init__(self)
    def my_method(self):
        print("Метод my_method() класса ChildClass")
        # ParentClass.my_method(self)
        super().my_method()

# c = ChildClass()
# c.my_method()

            # @property

class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property
    def my_method(self):
        return f"Параметры, переданные в класс: {self.param_1}, {self.param_2}"

# Результат:
# mc = MyClass("text_1", "text_2")
#
# print(mc.param_1)
# print(mc.param_2)
# attr = mc.my_method
# print(attr)

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__(self, list):   # Это конструктор типа входные аргументы в класс
        self.list = list

    def __str__(self): # это типа Принт из КЛАССА чего нужно
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        list_three = []
        for i in range(len(self.list)):
            list_three.append([])
            for j in range(len(self.list)):
                list_three[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, list_three))

    # Результат

matr_one = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matr_two = [[4, 4, 4], [5, 5, 5], [6, 6, 6]]

mat_1 = Matrix(matr_one)
mat_2 = Matrix(matr_two)

print(mat_1, '\n')
print(mat_2, '\n')
print(mat_1 + mat_2) # Выполнение метода def __add__(self, other):

