from time import time as current_time

from base_clock import BaseClock
from clock_face import ClockFace
from arrow import Arrow
from clock_time import Time


class AnalogClock(BaseClock):
    """Класс круглых стрелочных часов"""
    def __init__(self, *args):
        start_time = current_time()  # Нужно для компенсации потерь времени на инициализацию
        super().__init__(*args)
        self.time = Time(self.time, limiter=(12, 60, 60, 1000))
        self._radius = min(self.size) // 2 * 0.95
        self._center = (self.location[0] + self.size[0] / 2,
                        self.location[1] + self.size[1] / 2)
        self._clock_face = ClockFace(self._radius, self._center)
        self._hour_arrow = Arrow(
            self._center, self._radius // 3, self._radius / 20, self.time.hour, 12
        )
        self._minute_arrow = Arrow(
            self._center, self._radius * 0.65, self._radius / 30, self.time.minute, 60, self._hour_arrow
        )
        self._second_arrow = Arrow(
            self._center, self._radius * 0.75, self._radius / 40, round(self.time.second), 60, self._minute_arrow
        )
        # Компенсация потерь времени на инициализацию
        self.time += current_time() - start_time
        self.update()

    def set_time(self, time):
        super().set_time(time)
        self.update()

    def set_hour(self, hour):
        super().set_hour(hour)
        self.update()

    def set_minute(self, minute):
        super().set_minute(minute)
        self.update()

    def set_second(self, second):
        super().set_second(second)
        self.update()

    def update(self):
        self._second_arrow.set_position(round(self.time.second))
        self._minute_arrow.set_position(self.time.minute)
        self._hour_arrow.set_position(self.time.hour)
