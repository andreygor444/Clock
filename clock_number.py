from math import log10
from turtle import Turtle

from clock_digit import ClockDigit


class ClockNumber:
    """Представляет число на циферблате/экране часов"""
    def __init__(self, value, location: tuple, size: int = 30, length=None):
        """
        :param value: Само число, тип int
        :param location: Координаты центра числа, кортеж вида (x, y)
        :param size: Высота числа в пикселях
        :param length: Количество цифр в числе. При наличии данного аргумента число будет дополнено
                       нулями слева так, чтобы количетво цифр равнялось length
        """
        self.value = value
        self.location = location
        self.height = size
        if length is None:
            try:
                self._length = int(log10(value)) + 1
            except ValueError:  # Возникает при value = 0
                self._length = 1
        else:
            self._length = length
        self.width = size * 0.6 * self._length - 0.1
        self._make_digits()

    def _make_digits(self):
        self._digits = []
        for i in range(self._length):
            digit = self.value % 10 ** (self._length - i) // 10 ** (self._length - i - 1)
            digit_location = (self.location[0] - self.width / 2 + 0.6 * self.height * (i + 0.5), self.location[1])
            digit_ = ClockDigit(digit, digit_location, self.height)
            self._digits.append(digit_)

    def set_value(self, value):
        self.value = value
        for i in range(self._length):
            digit = self.value % 10 ** (self._length - i) // 10 ** (self._length - i - 1)
            self._digits[i].set_value(digit)

    def to_int(self):
        return self.value
