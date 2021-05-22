from turtle import Turtle

from Time import Time
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

    def main_loop(self, update_interval=1, threaded=False):
        """
        Основной цикл часов, в котором время бесконечно обновляется с некоторым интервалом
        :param update_interval: Интервал обновления времени
        :param threaded: Запускает данный процесс в отдельном потоке
        """
        pass
