from abc import ABC, abstractmethod
from io import StringIO


def convert_arabic_to_roman(number: int) -> str:
    print(number)
    m: int = number // 1000
    s: str = ""
    s = s + "M" * m
    mr: int = number % 1000
    print(mr)
    c: int = mr // 100
    if c == 9:
        s = s + "CM"
    elif 5 <= c < 9:
        s = s + "D" + "C" * (c-5)
    elif c == 4:
        s = s + "CD"
    else:
        s = s + "C" * c
    cr: int = mr % 100
    print(cr)
    x: int = cr // 10
    if x == 9:
        s = s + "XC"
    elif 5 <= x < 9:
        s = s + "L" + "X" * (x-5)
    elif x == 4:
        s = s + "XL"
    else:
        s = s + "X" * x
    xr: int = cr % 10
    print(xr)
    i: int = xr
    if i == 9:
        s = s + "IX"
    elif 5 <= i < 9:
        s = s + "V" + "I" * (i - 5)
    elif i == 4:
        s = s + "IV"
    else:
        s = s + "I" * i
    return s



def convert_roman_to_arabic(number: str) -> int:
    i = 0
    for j in range(len(number)):
        match number[j]:
            case 'I':
                i = i + 1
            case 'V':
                i = i + 5
                if j != 0:
                    if number[j-1] == 'I':
                        i = i - 2
            case 'X':
                i = i + 10
                if j != 0:
                    if number[j - 1] == 'I':
                        i = i - 2
            case 'L':
                i = i + 50
                if j != 0:
                    if number[j - 1] == 'X':
                        i = i - 20
            case 'C':
                i = i + 100
                if j != 0:
                    if number[j - 1] == 'X':
                        i = i - 20
            case 'D':
                i = i + 500
                if j != 0:
                    if number[j - 1] == 'C':
                        i = i - 200
            case 'M':
                i = i + 1000
                if j != 0:
                    if number[j - 1] == 'C':
                        i = i - 200
    return i


def average_age_by_position(file):
    pass


"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""
class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""

    pass


class CSVWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    pass


class YAMLWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""

    pass


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""

        self.data = data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""

        pass
