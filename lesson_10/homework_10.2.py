#Завдання 2

#Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
#Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
#Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
#Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return self.__side * 4


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return round(math.pi * self.__radius ** 2, 2)

    def get_perimeter(self):
        return round(2 * math.pi * self.__radius, 2)


figures = [
    Square(4),
    Rectangle(5, 3),
    Circle(2)
]

for figure in figures:
    print(f"Фігура: {figure.__class__.__name__}")
    print(f"Площа = {figure.get_area()}")
    print(f"Периметр = {figure.get_perimeter()}")
    print("-" * 20)