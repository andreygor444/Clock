from turtle import Terminator
from _tkinter import TclError
from functools import reduce


def can_exit_while_drawing(func):
    """
    turtle выкидывает ошибку когда окно закрывается во время отрисовки объекта.
    Этот декоратор позволяет игнорировать данную ошибку
    """
    def new_func(*args):
        try:
            func(*args)
        except (Terminator, TclError):
            raise SystemExit

    return new_func


def product(sequence):
    """Возвращает Произведение всех элементов полученной последовательности"""
    assert isinstance(sequence, (list, tuple, set))
    return reduce(lambda a, b: a * b, sequence)
