import datetime


class Time:
    """Класс, отвечающий за время в часах"""
    def __init__(self, time, limiter=(24, 60, 60)):
        """
        :param time: Может быть экземпляром классов Time или datetime.time, кортежем или списком
        :param limiter: Ограничитель - кортеж из трёх элементов. Нужен для возможности устанавливать 12-часовой формат
        """
        if isinstance(time, Time):
            hour, minute, second = time.hour, time.minute, time.second
        elif isinstance(time, datetime.time):
            hour, minute, second = time.hour, time.minute, time.second + time.microsecond / 1000000
        elif isinstance(time, (tuple, list)):
            assert len(time) == 3, 'Wrong argument format'
            hour, minute, second = time
        else:
            raise TypeError('Wrong argument type')
        assert type(hour) == int and type(minute) == int and type(second) in (int, float), 'Wrong argument type'
        self._limiter = limiter
        self.hour = hour % self._limiter[0]
        self.minute = minute % self._limiter[1]
        self.second = second % self._limiter[2]

    def set_hour(self, hour):
        assert 0 <= hour < self._limiter[0], 'Too big value'
        self.hour = hour

    def set_minute(self, minute):
        assert 0 <= minute < self._limiter[1], 'Too big value'
        self.minute = minute

    def set_second(self, second):
        assert 0 <= second < self._limiter[2], 'Too big value'
        self.second = second

    def add_hours(self, hours):
        hours = int(hours)
        self.hour = (self.hour + hours) % self._limiter[0]

    def add_minutes(self, minutes):
        minutes = int(minutes)
        self.minute += minutes
        self.add_hours(self.minute // self._limiter[1])
        self.minute %= self._limiter[1]

    def add_seconds(self, seconds):
        self.second += seconds
        self.add_hours(self.second // (self._limiter[1] * self._limiter[2]))
        self.add_minutes(self.second // self._limiter[2])
        self.second %= self._limiter[2]

    def __add__(self, other):
        """
        :param other: Прибавляемое время. Может быть типом int, float, Time, datetime.time, tuple или list
        :return: Time
        """
        if isinstance(other, (int, float)):
            hours, minutes, seconds = 0, 0, other
        elif isinstance(other, (tuple, list)):
            assert len(other) == 3, 'Wrong argument type'
            hours, minutes, seconds = other
        elif isinstance(other, (Time, datetime.time)):
            hours, minutes, seconds = other.hour, other.minute, other.second
        else:
            raise TypeError('Wrong argument type')
        assert type(hours) == int and type(minutes) == int and type(seconds) in (int, float), 'Wrong argument type'
        self.add_seconds(seconds)
        self.add_minutes(minutes)
        self.add_hours(hours)
        return self

    def __str__(self):
        return f'{self.hour}:{self.minute}:{int(self.second)}'
