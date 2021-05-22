from turtle import Turtle
from time import time as current_time

from base_clock import BaseClock
from clock_number import ClockNumber
from clock_time import Time


class DigitalClock(BaseClock):
    """Класс цифровых часов"""
    def __init__(self, *args, hour_format=24):
        start_time = current_time()  # Нужно для компенсации потерь времени на инициализацию
        super().__init__(*args)
        self.time = Time(self.time, limiter=(hour_format, 60, 60, 1000))
        number_height = min(self.size[0] * 0.22, self.size[1] * 0.8)
        center = (self.location[0] + self.size[0] / 2,
                  self.location[1] + self.size[1] / 2)
        self._minute_number = ClockNumber(
            self.time.minute, center, number_height, 2
        )
        number_width = self._minute_number.width
        self._hour_number = ClockNumber(
            self.time.hour, (center[0] - number_width * 1.3, center[1]), number_height, 2
        )
        self._second_number = ClockNumber(
            self.time.second, (center[0] + number_width * 1.3, center[1]), number_height, 2
        )
        # Компенсация потерь времени на инициализацию
        self.time += current_time() - start_time
        self.update()

    def _draw_frame(self):
        super()._draw_frame()
        # Отрисовка двоеточий
        t = Turtle()
        t.speed(0)
        x_bias = min(self.size[0] * 0.17, self.size[1] * 0.62)
        y_bias = min(self.size[0] * 0.07, self.size[1] * 0.25)
        for x in -1, 1:
            for y in -1, 1:
                t.up()
                t.goto((self.location[0] + self.size[0] / 2 + x_bias * x,
                        self.location[1] + self.size[1] / 2 + y_bias * y))
                t.down()
                t.dot(min(self.size[0] // 70, self.size[1] // 19.25))
        t.hideturtle()

    def update(self):
        self._hour_number.set_value(self.time.hour)
        self._minute_number.set_value(self.time.minute)
        self._second_number.set_value(self.time.second)
