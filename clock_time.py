import datetime

from utils import product


class Time:
    """Класс, отвечающий за время в часах"""
    def __init__(self, time, limiter=(24, 60, 60, 1000)):
        """
        :param time: Может быть экземпляром классов Time или datetime.time, кортежем или списком
        :param limiter: Ограничитель, кортеж из четырёх элементов. Нужен для возможности устанавливать 12-часовой формат
        """
        if isinstance(time, Time):
            hour, minute, second, millisecond = time.hour, time.minute, time.second, time.millisecond
        elif isinstance(time, datetime.time):
            hour, minute, second, millisecond = time.hour, time.minute, time.second, time.microsecond // 1000
        elif isinstance(time, (tuple, list)):
            assert len(time) == 4, 'Wrong argument format'
            hour, minute, second, millisecond = time
        else:
            raise TypeError('Wrong argument type')
        assert all(isinstance(i, int) for i in (hour, minute, second, millisecond)), 'Wrong argument type'
        assert len(limiter) == 4, 'Wrong argument format'
        self._limiter = limiter
        self.hour = hour % self._limiter[0]
        self.minute = minute % self._limiter[1]
        self.second = second % self._limiter[2]
        self.millisecond = millisecond % self._limiter[3]

    def set_hour(self, hour):
        assert isinstance(hour, int), 'Wrong argument type'
        assert 0 <= hour < self._limiter[0], 'Too big value'
        self.hour = hour

    def set_minute(self, minute):
        assert isinstance(minute, int), 'Wrong argument type'
        assert 0 <= minute < self._limiter[1], 'Too big value'
        self.minute = minute

    def set_second(self, second):
        assert isinstance(second, int), 'Wrong argument type'
        assert 0 <= second < self._limiter[2], 'Too big value'
        self.second = second

    def add_hours(self, hours):
        self.add_milliseconds(hours * product(self._limiter[1:]))

    def add_minutes(self, minutes):
        self.add_milliseconds(minutes * product(self._limiter[2:]))

    def add_seconds(self, seconds):
        self.add_milliseconds(seconds * self._limiter[3])

    def add_milliseconds(self, milliseconds):
        milliseconds = int(milliseconds)
        self.millisecond += milliseconds
        self.second += self.millisecond // self._limiter[3]
        self.millisecond %= self._limiter[3]

        self.minute += self.second // self._limiter[2]
        self.second %= self._limiter[2]

        self.hour += self.minute // self._limiter[1]
        self.minute %= self._limiter[1]
        self.hour %= self._limiter[0]

    def __add__(self, other):
        """
        :param other: Прибавляемое время. Может быть любым типом, преобразовываемым в Time
        :return: Time
        """
        if isinstance(other, (int, float)):
            seconds, milliseconds = int(other), other % 1 * self._limiter[3]
            self.add_milliseconds(milliseconds)
            self.add_seconds(seconds)
            return self
        try:
            other = Time(other)
        except (AssertionError, TypeError):
            raise TypeError('Wrong argument type/format')
        self.add_milliseconds(other.millisecond)
        self.add_seconds(other.second)
        self.add_minutes(other.minute)
        self.add_hours(other.hour)
        return self

    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}:{self.millisecond}'
