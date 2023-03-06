import turtle as tl
from . import trunk_left_right  # Подключение модуля из своего пакета


def trunk(size):
    """
    Построение всего ствола
    """
    x0, y0 = tl.xcor(), tl.ycor()
    tl.color('black', 'brown')
    tl.begin_fill()
    trunk_left_right.trunk_left(size, 0)  # Использована функция из модуля
    x1, y1 = tl.xcor(), tl.ycor()
    tl.penup()
    tl.goto(x0, y0)
    tl.pendown()
    tl.goto(x0 + 50, y0)
    tl.setheading(0)
    trunk_left_right.trunk_right(size, 0)  # Использована функция из модуля
    tl.goto(x1, y1)
    tl.end_fill()
