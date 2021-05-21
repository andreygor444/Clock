from turtle import Turtle
from ClockNumber import ClockNumber
from math import sin, cos, pi


class ClockFace:
    def __init__(self, radius, center, numbers_count=12):
        self.radius = radius
        self._center = center
        self._turtle = Turtle()
        self._turtle.speed(0)
        self._redraw()
        self._make_numbers(numbers_count)

    def _redraw(self):
        t = self._turtle
        t.reset()
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
        bias = self.radius / 20
        for i in range(1, numbers_count + 1):
            angle = pi * 2 / numbers_count * i
            x = self._center[0] + self.radius * 0.8 * sin(angle) + bias
            y = self._center[1] + self.radius * 0.8 * cos(angle) + bias * 1.8
            number = ClockNumber(i, (x, y), number_size)
            self._numbers.append(number)
