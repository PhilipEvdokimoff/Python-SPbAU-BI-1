import turtle as tl
from .components.trunk_pack import trunk  # Подключение модуля на два уровня глубже
from .components import coconuts  # Подключение модуля на уровень глубже
from .components.leaves_pack import leaves  # Подключение модуля на два уровня глубже


def palm(size, angle, n_leaves):
    """
    Построение всей пальмы
    """
    trunk.trunk(size)  # Использована функция из модуля
    node = (tl.xcor() + 10, tl.ycor())
    tl.penup()
    tl.left(75)
    tl.backward(75)
    tl.pendown()
    coconuts.coconuts(size)  # Использована функция из модуля
    tl.goto(node)
    tl.left(21)
    leaves.leaves(size, angle, n_leaves)  # Использована функция из модуля
