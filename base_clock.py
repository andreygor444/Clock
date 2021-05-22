from turtle import Turtle
from time import sleep, time as current_time

from clock_time import Time
from utils import can_exit_while_drawing


class BaseClock:
    """Абстрактный класс часов для наследования"""
    def __init__(self, location=(0, 0), size=(400, 300), time=(0, 0, 0)):
        """
        :param location: Координаты левого нижнего угла часов, кортеж вида (x, y)
        :param size: Размер часов, кортеж вида (x, y)
        :param time: Время. Любой тип, преобразуемый в Time
        """
        self.time = Time(time)
        self.location = location
        self.size = size
        self._draw_frame()

    @can_exit_while_drawing
    def _draw_frame(self):
        """Отрисовывает прямоугольный каркас часов"""
        t = Turtle()
        t.speed(0)
        t.width(min(self.size[0] // 200, self.size[1] // 50))
        t.up()
        t.goto(self.location)
        t.down()
        for i in range(4):
            t.fd(self.size[i % 2])
            t.left(90)
        t.hideturtle()

    def set_time(self, time):
        self.time = Time(time)

    def set_hour(self, hour):
        self.time.set_hour(hour)

    def set_minute(self, minute):
        self.time.set_minute(minute)

    def set_second(self, second):
        self.time.set_second(second)

    def update(self):
        """Обновлет отображение часов в соответствии с временем на часах"""

    def main_loop(self, update_interval=1):
        """
        Основной цикл часов, в котором время бесконечно обновляется с некоторым интервалом
        :param update_interval: Интервал обновления времени
        """
        start_time = current_time()
        while True:
            while current_time() - start_time < update_interval * 0.9:
                sleep(update_interval / 10)
            while current_time() - start_time < update_interval:
                sleep(update_interval / 100)
            self.time += current_time() - start_time
            start_time = current_time()
            self.update()
