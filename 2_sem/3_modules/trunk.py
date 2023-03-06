import turtle as tl
import trunk_left_right


def trunk(size):
    """
    Построение всего ствола
    """
    x0, y0 = tl.xcor(), tl.ycor()
    tl.color('black', 'brown')
    tl.begin_fill()
    trunk_left_right.trunk_left(size, 0)  # !!! ИСПОЛЬЗОВАН МОДУЛЬ !!!
    x1, y1 = tl.xcor(), tl.ycor()
    tl.penup()
    tl.goto(x0, y0)
    tl.pendown()
    tl.goto(x0 + 50, y0)
    tl.setheading(0)
    trunk_left_right.trunk_right(size, 0)  # !!! ИСПОЛЬЗОВАН МОДУЛЬ !!!
    tl.goto(x1, y1)
    tl.end_fill()
