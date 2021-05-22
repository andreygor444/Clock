from AnalogClock import AnalogClock
import datetime


def main():
    clock_position = (-400, -300)
    clock_size = (800, 600)
    time = datetime.datetime.now().time()
    clock = AnalogClock(clock_position, clock_size, time)
    clock.main_loop(1)


if __name__ == '__main__':
    main()
