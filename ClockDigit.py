from turtle import Turtle


class ClockDigit:
    _segments = {
        0: (0, 2, 6, 8),
        1: (0, 2, 3, 5, 6, 8, 9),
        2: (0, 1, 3, 4, 5, 6, 7, 8, 9),
        3: (0, 1, 2, 3, 4, 7, 8, 9),
        4: (0, 2, 3, 5, 6, 7, 8, 9),
        5: (0, 4, 5, 6, 8, 9),
        6: (2, 3, 4, 5, 6, 8, 9)
    }

    def __init__(self, number, location: tuple, size: int = 30):
        self.number = number
        self.location = location
        self.height = size
        self.width = size / 2
        self._turtle = Turtle()
        self._turtle.speed(10)
        self._redraw()

    def _redraw(self):
        t = self._turtle
        t.reset()
        t.up()
        t.goto((self.location[0] - self.width / 2, self.location[1] - self.height / 2))
        t.seth(-90)
        t.down()
        step = self.width
        for segment, digits_that_have_segment in ClockDigit._segments.items():
            if self.number not in digits_that_have_segment:
                t.up()
            t.fd(step)
            t.down()
            if segment != 2:
                t.left(90)
        t.hideturtle()

    def to_int(self):
        return self.number
