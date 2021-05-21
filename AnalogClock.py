from time import sleep

from BaseClock import BaseClock
from ClockFace import ClockFace
from Arrow import Arrow


class AnalogClock(BaseClock):
    def __init__(self, location=(0, 0), size=(400, 300), time=(0, 0, 0)):
        self.location = location
        self.size = size
        super().set_time(time)
        self._radius = min(self.size) // 2 * 0.95
        self._center = (self.location[0] + self.size[0] // 2,
                        self.location[1] + self.size[1] // 2)
        self._clock_face = ClockFace(self._radius, self._center)
        self._hour_arrow = Arrow(self._center, self._radius // 3, self._radius / 20, self.time.hour)
        self._minute_arrow = Arrow(self._center, self._radius * 0.65, self._radius / 30, self.time.minute, 60, self._hour_arrow)
        self._second_arrow = Arrow(self._center, self._radius * 0.75, self._radius / 40, self.time.second, 60, self._minute_arrow)
        self._draw_frame()

    def set_hour(self, hour):
        super().set_hour(hour)
        self.synch_arrows()

    def set_minute(self, minute):
        super().set_minute(minute)
        self.synch_arrows()

    def set_second(self, second):
        super().set_second(second)
        self.synch_arrows()

    def synch_arrows(self):
        self._second_arrow.set_state(self.time.second)
        self._minute_arrow.set_state(self.time.minute)
        self._hour_arrow.set_state(self.time.hour)

    def main_loop(self, update_interval=1, threaded=False):
        if threaded:
            Thread(target=self.main_loop, args=[update_interval]).start()
            return
        while True:
            sleep(update_interval)
            self.time += update_interval
            self.synch_arrows()
