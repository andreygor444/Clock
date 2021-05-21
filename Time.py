from typing import Tuple, Union


class Time:
    def __init__(self, hour=0, minute=0, second=0, limiter=(24, 60, 60)):
        assert isinstance(hour, int), 'Wrong argument type'
        assert isinstance(minute, int), 'Wrong argument type'
        assert isinstance(second, int), 'Wrong argument type'
        self.hour = hour
        self.minute = minute
        self.second = second
        self._limiter = limiter

    def set_hour(self, hour):
        assert 0 <= hour < self._limiter[0], "Too big value"
        self.hour = hour

    def set_minute(self, minute):
        assert 0 <= minute < self._limiter[1], "Too big value"
        self.minute = minute

    def set_second(self, second):
        assert 0 <= second < self._limiter[2], "Too big value"
        self.second = second

    def add_hours(self, hours):
        self.hour = (self.hour + hours) % self._limiter[0]

    def add_minutes(self, minutes):
        self.minute += minutes
        self.add_hours(self.minute // self._limiter[1])
        self.minute %= self._limiter[1]

    def add_seconds(self, seconds):
        self.second += seconds
        self.add_hours(self.second // (self._limiter[1] * self._limiter[2]))
        self.add_minutes(seconds // self._limiter[2])
        self.second %= self._limiter[2]

    def __add__(self, other):
        if isinstance(other, int):
            hours, minutes, seconds = 0, 0, other
        elif isinstance(other, tuple):
            hours, minutes, seconds = other
        elif isinstance(other, Time):
            hours, minutes, seconds = other.hour, other.minute, other.second
        else:
            raise TypeError('Wrong argument type')
        self.add_seconds(seconds)
        self.add_minutes(minutes)
        self.add_hours(hours)
        return self
