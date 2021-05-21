from turtle import Turtle
from typing import Tuple, Union
from Time import Time


class BaseClock:
    def __init__(self, location=(0, 0), size=(400, 300), time: Union[Tuple[int], Time] = (0, 0, 0)):
        self.location = location
        self.size = size
        self.set_time(time)
        self._draw_frame()

    def _draw_frame(self):
        t = Turtle()
        t.up()
        t.goto(self.location)
        t.down()
        for i in range(4):
            t.fd(self.size[i % 2])
            t.left(90)
        t.hideturtle()

    def set_time(self, time):
        if isinstance(time, Time):
            self.time = time
        else:
            try:
                self.time = Time(*time)
            except (TypeError, AssertionError):
                raise TypeError("Wrong argument type")

    def set_hour(self, hour):
        self.time.set_hour(hour)

    def set_minute(self, minute):
        self.time.set_minute(minute)

    def set_second(self, second):
        self.time.set_second(second)

    def main_loop(self, update_interval=1, threaded=False):
        pass
