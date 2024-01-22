import doctest
from string import ascii_letters
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов

class Car:
    def __init__(self, brand: str, color: str, max_speed: Union[int, float]):
        """
        Создание и подготовка к работе объекта машина
        :param brand: Брэнд автомобиля
        :param color: Цвет автомобиля
        :param max_speed: Максимальная скорость автомобиля
        Примеры:
        >>> car_1 = Car('BMW', 'green', 320) # инициализация экземпляра класса
        """
        self.max_speed = None
        self.brand = None
        self.color = None
        self.init_brand(brand)
        self.init_color(color)
        self.init_max_speed(max_speed)

    def init_brand(self, brand: str):
        """
        Проверка правильного ввода брэнда
        :param brand: Брэнд автомобиля
        Примеры:
        >>> car_1 = Car('BMW', 'green', 320)
        >>> car_1.brand
        'BMW'
        """
        if not isinstance(brand, str) or not brand.isalpha():
            raise TypeError('Брэнд должен содержать буквы!')
        self.brand = brand

    def init_color(self, color: str):
        """
        Проверка правильного ввода цвета
        :param color: Цвет автомобиля
        Примеры:
        >>> car_1 = Car('BMW', 'green', 320)
        >>> car_1.color
        'green'
        """
        if not isinstance(color, str) or not color.isalpha():
            raise TypeError('Цвет должен содержать буквы!')
        self.color = color

    def init_max_speed(self, speed: (int, float)):
        """
        Проверка правильного ввода скорости
        :param speed: Максимальная скорость автомобиля
        Примеры:
        >>> car_1 = Car('BMW', 'green', 320)
        >>> car_1.max_speed
        320
        """
        if not isinstance(speed, Union[int, float]) or speed < 0:
            raise ValueError('Скорость измеряется положительным числом!')
        self.max_speed = speed

class Table:
    def __init__(self, material: str, height: Union[int, float], length: Union[int, float]):
        """
        Создание и подготовка к работе объекта стол
        :param material: Материал стола
        :param height: Высота стола
        :param length: Длина стола
        Примеры:
        >>> table = Table('tree', 80.5, 140) # инициализация экземпляра класса
        """

        self.material = None
        self.height = None
        self.length = None
        self.init_material(material)
        self.init_height(height)
        self.init_length(length)

    def init_material(self, material: str):
        """
        Проверка правильности ввода материала
        :param material: Материал стола
        >>> table = Table('tree', 80.5, 140)
        >>> table.material
        'tree'
        """
        if not isinstance(material, str) or not material.isalpha():
            raise TypeError('Материал стола должен содержать буквы!')
        self.material = material

    def init_height(self, height: Union[int, float]):
        """
        Проверка правильности ввода высоты стола
        :param height: Высота стола
        >>> table = Table('tree', 80.5, 140)
        >>> table.height
        80.5
        """
        if not isinstance(height, Union[int, float]) or height < 0:
            raise ValueError('Высота стола не может быть отрицательным числом'
                             ' и содержать буквенные символы!')
        self.height = height

    def init_length(self, length: Union[int, float]):
        """
        Проверка правильности ввода длины стола
        :param length: Высота стола
        >>> table = Table('tree', 80.5, 140)
        >>> table.length
        140
        """
        if not isinstance(length, Union[int, float]) or length < 0:
            raise ValueError('Длина стола не может быть отрицательным числом'
                             ' и содержать буквенные символы!')
        self.length = length

class Computer:
    def __init__(self, operating_system: str, screen_diagonal: Union[int, float], ram_memory: int):
        """
        Создание и подготовка к работе объекта компьютер
        :param operating_system: Операционная система компьютера
        :param screen_diagonal: Диагональ экрана компьютера
        :param ram_memory: Размер оперативной памяти компьютера
        Пример:
        >>> comp = Computer('Windows', 14.3, 16)
        """

        self.operating_system = None
        self.screen_diagonal = None
        self.ram_memory = None
        self.init_operating_system(operating_system)
        self.init_screen_diagonal(screen_diagonal)
        self.init_ram_memory(ram_memory)

    def init_operating_system(self, operating_system: str):
        """
        Проверка правильности ввода операционной системы компьютера
        :param operating_system: Операционная система компьютера
        >>> comp = Computer('Windows', 14.3, 16)
        >>> comp.operating_system
        'Windows'
        """
        if not isinstance(operating_system, str) or not operating_system.isalpha():
            raise TypeError('Операционная система должна быть в буквенном виде!')
        if operating_system in ascii_letters:
            raise TypeError('Название операционной системы должно состоять из латинских букв!')
        self.operating_system = operating_system

    def init_screen_diagonal(self, screen_diagonal: Union[int, float]):
        """
        Проверка правильности ввода диагонали экрана компьютера
        :param screen_diagonal: Диагональ экрана компьютера
        >>> comp = Computer('Windows', 14.3, 16)
        >>> comp.screen_diagonal
        14.3
        """
        if not isinstance(screen_diagonal, Union[int, float]) or screen_diagonal < 0:
            raise ValueError('Диагональ экрана компьютера не может содержать буквы'
                             ' и быть отрицательным числом!')
        self.screen_diagonal = screen_diagonal

    def init_ram_memory(self, ram_memory: int):
        """
        Проверка правильности ввода оперативной памяти компьютера
        :param ram_memory: Размер оперативной памяти компьютера
        >>> comp = Computer('Windows', 14.3, 16)
        >>> comp.ram_memory
        16
        """
        if not isinstance(ram_memory, int) or ram_memory < 0:
            raise TypeError('Оперативная память компьютера должна содержать целое число'
                            ' и не может быть отрицательным')
        self.ram_memory = ram_memory

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
