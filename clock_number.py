from math import log10

from clock_digit import ClockDigit


class ClockNumber:
    """Представляет число на циферблате/экране часов"""
    def __init__(self, number, location: tuple, size: int = 30):
        """
        :param number: Само число, тип int
        :param location: Координаты центра числа: кортеж вида (x, y)
        :param size: Высота числа в пикселях
        """
        self.number = number
        self.location = location
        self.height = size
        self._digits_count = int(log10(number)) + 1
        self.width = self._digits_count * size * 0.6
        self._make_digits()

    def _make_digits(self):
        self._digits = []
        for i in range(self._digits_count):
            digit = self.number % 10 ** (self._digits_count - i) // 10 ** (self._digits_count - i - 1)
            digit_location = (self.location[0] - self.width / 2 + 0.6 * self.height * i, self.location[1])
            digit_ = ClockDigit(digit, digit_location, self.height)
            self._digits.append(digit_)

    def to_int(self):
        return self.number
