from turtle import Turtle
from ClockNumber import ClockNumber
from math import sin, cos, pi

from utils import can_exit_while_drawing


class ClockFace:
    """Класс циферблата часов"""
    def __init__(self, radius, center, numbers_count=12):
        self.radius = radius
        self._center = center
        self._render()
        self._make_numbers(numbers_count)

    @can_exit_while_drawing
    def _render(self):
        """Отрисовывает круглый контур циферблата и точку в центре"""
        t = Turtle()
        t.speed(0)
        t.up()
        t.goto((self._center[0], self._center[1] - self.radius))
        t.seth(0)
        t.down()
        t.circle(self.radius)
        t.up()
        t.goto((self._center[0], self._center[1] - self.radius / 30))
        t.down()
        t.color('black', 'black')
        t.begin_fill()
        t.circle(self.radius / 30)
        t.end_fill()
        t.hideturtle()

    def _make_numbers(self, numbers_count):
        self._numbers = []
        number_size = self.radius / 6
        x_bias = self.radius * 0.05
        y_bias = self.radius * 0.09
        # Чтобы цифры стояли ровно, приходится их немного смещать вверх и вправо
        for i in range(1, numbers_count + 1):
            angle = pi * 2 / numbers_count * i
            x = self._center[0] + self.radius * 0.8 * sin(angle) + x_bias
            y = self._center[1] + self.radius * 0.8 * cos(angle) + y_bias
            number = ClockNumber(i, (x, y), number_size)
            self._numbers.append(number)
