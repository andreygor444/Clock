from turtle import Turtle
from typing import Tuple
import math

from utils import can_exit_while_drawing


class Arrow:
    """Класс, описывающий часовую стрелку"""
    def __init__(self, base: Tuple[int, int], length, width, position=0, positions_count=60, dependent_arrow=None):
        """
        :param base: Координаты основания стрелки - кортеж вида (x, y)
        :param length: Длина стрелки
        :param width: Ширина стрелки
        :param position: Текущее положение стрелки, вещественное число от нуля до positions_count
        :param positions_count: Количество положений, принимаемых стрелкой
        :param dependent_arrow: Зависимая стрелка. Будет сдвигаться на одну позицию каждый раз,
                                когда эта стрелка проходит через своё нулевое состояние
        """
        assert length > 0 and isinstance(length, (int, float)), "length must be positive number"
        assert width > 0 and isinstance(width, (int, float)), "width must be positive number"
        self._base = base
        self.length = length
        self._width = width
        self.position = position
        self.positions_count = positions_count
        self._dependent_arrow = dependent_arrow
        self._turtle = Turtle()  # У стрелки будет своя черепаха

        self._angle = math.degrees(math.atan2(length, width / 2))
        self._side_length = math.hypot(self._width / 2, self.length)
        # Стрелка выглядит как равнобедренный треугольник.
        # _angle - угол при основании этого треугольника, _side_length - длина ребра
        self._render()

    @can_exit_while_drawing
    def _render(self):
        t = self._turtle
        t.reset()
        t.speed(0)
        t.up()
        t.goto(self._base)
        t.seth(-360 / self.positions_count * self.position - 180)
        t.fd(self._width / 2)
        t.right(180 - self._angle)
        t.down()
        t.fd(self._side_length)
        t.right(180 - (90 - self._angle) * 2)
        t.fd(self._side_length)
        t.hideturtle()

    def set_position(self, position):
        assert 0 <= position < self.positions_count, "Position out of range"
        if position == self.position:
            return
        self.position = position
        self._render()
