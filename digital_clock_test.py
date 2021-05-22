from digital_clock import DigitalClock
import datetime


def main():
    clock_position = (-400, -100)
    clock_size = (800, 200)
    time = datetime.datetime.now().time()
    digital_clock = DigitalClock(clock_position, clock_size, time, hour_format=24)
    digital_clock.main_loop(1)


if __name__ == '__main__':
    main()
