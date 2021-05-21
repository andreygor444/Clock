from turtle import Turtle
from typing import Tuple
from math import atan2, degrees, hypot


class Arrow:
    def __init__(self, base: Tuple[int], length, width, state=0, states_count=60, dependent_arrow=None):
        assert length > 0 and isinstance(length, (int, float)), "length must be positive number"
        assert width > 0 and isinstance(width, (int, float)), "width must be positive number"
        self._base = base
        self.length = length
        self._width = width
        self.state = state
        self.states_count = states_count
        self._dependent_arrow = dependent_arrow
        self._turtle = Turtle()
        self._turtle.speed(8)

        self._angle = degrees(atan2(length, width / 2))
        self._side_length = hypot(self._width / 2, self.length)
        # Стрелка выглядит как равнобедренный треугольник.
        # _angle - угол при основании этого треугольника, _side_length - длина ребра
        self._redraw()

    def _redraw(self):
        t = self._turtle
        t.reset()
        t.up()
        t.goto(self._base)
        t.seth(360 / self.states_count * self.state - 180)
        t.fd(self._width / 2)
        t.right(180 - self._angle)
        t.down()
        t.fd(self._side_length)
        t.right(180 - (90 - self._angle) * 2)
        t.fd(self._side_length)
        t.hideturtle()

    def set_state(self, state):
        assert 0 <= state < self.states_count
        if state == self.state:
            return
        self.state = state
        self._redraw()

    def move(self, moves=1):
        direction = moves // abs(moves)
        for i in range(self.state + direction, self.state + direction + moves, direction):
            self.set_state(i % self.states_count)
            if not self.state:
                self._dependent_arrow.move(direction)
