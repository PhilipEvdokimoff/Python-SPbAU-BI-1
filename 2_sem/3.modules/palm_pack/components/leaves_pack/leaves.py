import turtle as tl
import leaf_up_down  # Подключение модуля на одном уровне


def leaves(size, angle, n_leaves):
    """
    Построение всех листьев
    """
    if n_leaves > 0:
        tl.color('black', 'green')
        tl.begin_fill()
        heading = tl.heading()
        x0, y0 = tl.xcor(), tl.ycor()
        leaf_up_down.leaf_up(size, angle, 11)  # Использована функция из модуля
        x1, y1 = tl.xcor(), tl.ycor()
        tl.penup()
        tl.goto(x0, y0)
        tl.pendown()
        tl.setheading(heading)
        leaf_up_down.leaf_down(size, angle, 11)  # Использована функция из модуля
        tl.left(15.849)
        tl.forward(50)
        tl.goto(x1, y1)
        tl.end_fill()
        tl.penup()
        tl.goto(x0, y0)
        tl.pendown()
        tl.setheading(heading)
        tl.right(56)
        leaves(size, angle, n_leaves - 1) # Рекурсия
