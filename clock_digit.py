from turtle import Turtle

from utils import can_exit_while_drawing


class ClockDigit:
    _drawing_rule = {
        0: (0, 2, 6, 8),
        1: (0, 2, 3, 5, 6, 8, 9),
        2: (0, 1, 3, 4, 5, 6, 7, 8, 9),
        3: (0, 1, 2, 3, 4, 7, 8, 9),
        4: (0, 2, 3, 5, 6, 7, 8, 9),
        5: (0, 4, 5, 6, 8, 9),
        6: (2, 3, 4, 5, 6, 8, 9)
    }  # {сегмент_цифры: цифры_имеющие_данный_сегмент}
    # Правило отрисовки цифр: черепаха перемещается по спирали,
    # проходя каждый сегмент цифры, и, если нужно, проводит линию

    def __init__(self, value, location: tuple, size: int = 30):
        """
        :param value: Сама цифра, тип int
        :param location: Координаты центра цифры: кортеж вида (x, y)
        :param size: Высота цифры в пикселях
        """
        self.value = value
        self.location = location
        self.height = size
        self.width = size / 2
        self._turtle = Turtle()  # У цифры будет своя черепаха
        self._render()

    def set_value(self, value):
        if value == self.value:
            return
        self.value = value
        self._render()

    def to_int(self):
        return self.value

    @can_exit_while_drawing
    def _render(self):
        t = self._turtle
        t.reset()
        t.speed(0)
        t.width(self.height // 30)
        t.up()
        t.goto((self.location[0] - self.width / 2, self.location[1]))
        t.seth(-90)
        t.down()
        step = self.width
        for segment, digits_that_have_segment in ClockDigit._drawing_rule.items():
            if self.value not in digits_that_have_segment:
                t.up()
            t.fd(step)
            t.down()
            if segment != 2:
                t.left(90)
        t.hideturtle()
