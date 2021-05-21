from AnalogClock import AnalogClock


def main():
    clock = AnalogClock((-400, -300), (800, 600), (4, 15, 33))
    clock.main_loop()


if __name__ == '__main__':
    main()
