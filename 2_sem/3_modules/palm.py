import turtle as tl
import trunk
import coconuts
import leaves


def palm(size, angle, n_leaves):
    """
    Построение всей пальмы
    """
    trunk.trunk(size)  # !!! ИСПОЛЬЗОВАН МОДУЛЬ !!!
    node = (tl.xcor() + 10, tl.ycor())
    tl.penup()
    tl.left(75)
    tl.backward(75)
    tl.pendown()
    coconuts.coconuts(size)  # !!! ИСПОЛЬЗОВАН МОДУЛЬ !!!
    tl.goto(node)
    tl.left(21)
    leaves.leaves(size, angle, n_leaves)  # !!! ИСПОЛЬЗОВАН МОДУЛЬ !!!
