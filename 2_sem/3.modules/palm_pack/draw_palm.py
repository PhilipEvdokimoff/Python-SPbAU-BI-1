import turtle as tl
from . import palm  # Подключение модуля на одном уровне


def draw_palm(size, angle, n_leaves):
    """
    Приготовление к выполнению фунций
    """
    tl.delay(0) 
    tl.speed(100)
    tl.penup()
    tl.goto(40,-320)
    tl.pendown()
    palm.palm(size, angle, n_leaves)  # Использована функция из модуля
    tl.done()
