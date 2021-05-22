from time import sleep
from threading import Thread
from time import time as current_time

from BaseClock import BaseClock
from ClockFace import ClockFace
from Arrow import Arrow


class AnalogClock(BaseClock):
    def __init__(self, *args):
        start_time = current_time()  # Нужно для компенсации потерь времени на инициализацию
        super().__init__(*args)
        self._radius = min(self.size) // 2 * 0.95
        self._center = (self.location[0] + self.size[0] // 2,
                        self.location[1] + self.size[1] // 2)
        self._clock_face = ClockFace(self._radius, self._center)
        self._hour_arrow = Arrow(self._center, self._radius // 3, self._radius / 20, self.time.hour, 12)
        self._minute_arrow = Arrow(self._center, self._radius * 0.65, self._radius / 30, self.time.minute, 60,
                                   self._hour_arrow)
        self._second_arrow = Arrow(self._center, self._radius * 0.75, self._radius / 40, self.time.second, 60,
                                   self._minute_arrow)
        # Компенсация потерь времени на инициализацию
        self.time += current_time() - start_time

    def set_time(self, time):
        super().set_time(time)
        self.sync_arrows()

    def set_hour(self, hour):
        super().set_hour(hour)
        self.sync_arrows()

    def set_minute(self, minute):
        super().set_minute(minute)
        self.sync_arrows()

    def set_second(self, second):
        super().set_second(second)
        self.sync_arrows()

    def sync_arrows(self):
        """Устанавливает стрелки в соответствии с текущим временем"""
        self._second_arrow.set_position(self.time.second)
        self._minute_arrow.set_position(self.time.minute)
        self._hour_arrow.set_position(self.time.hour)

    def main_loop(self, update_interval=1, threaded=False):
        if threaded:
            Thread(target=self.main_loop, args=(update_interval,)).start()
            return
        while True:
            sleep(update_interval)
            self.time += update_interval
            start_time = current_time()
            self.sync_arrows()
            time_loss = current_time() - start_time  # Потеря времени на передвижение стрелок
            self.time += time_loss
