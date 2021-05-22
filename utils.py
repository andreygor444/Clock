from turtle import Terminator
from _tkinter import TclError


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
