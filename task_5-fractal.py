import turtle as tl

"""
Построение изображения пальмы при помощи рекурсии (фракталов)
"""

def trunk_left(size, tilt):
    """
    Построение левого контура ствола
    """
    if size > 40:
        tl.left(95)
        tl.forward(size)
        tl.right(150)
        tl.forward(size / 5)
        tl.left(55 + tilt)
        trunk_left(size - 5, tilt + 2) # Рекурсия

def trunk_right(size, tilt):
    """
    Построение правого контура ствола
    """
    if size > 40:
        tl.left(85)
        tl.forward(size)
        tl.left(150)
        tl.forward(size / 5)
        tl.right(235 - tilt)
        trunk_right(size - 5, tilt + 2) # Рекурсия

def trunk(size):
    """
    Построение всего ствола
    """
    x0, y0 = tl.xcor(), tl.ycor()
    tl.color('black', 'brown')
    tl.begin_fill()
    trunk_left(size, 0)
    x1, y1 = tl.xcor(), tl.ycor()
    tl.penup()
    tl.goto(x0, y0)
    tl.pendown()
    tl.goto(x0 + 50, y0)
    tl.setheading(0)
    trunk_right(size, 0)
    tl.goto(x1, y1)
    tl.end_fill()

def coconuts(size):
    """
    Построение кокосов
    """
    coco_size = size / 3
    if coco_size > 19:
        tl.color('black', 'black')
        tl.begin_fill()
        tl.circle(coco_size)
        tl.penup()
        tl.right(120)
        tl.forward(11)
        tl.pendown()
        tl.end_fill()
        coconuts(size - 10) # Рекурсия

def leaf_up(size, angle, times):
    """
    Построение верхней части листа
    """
    if times > 0:
        tl.left(angle)
        tl.forward(size - 20)
        tl.right(angle + 2.5)
        tl.forward(size - 35)
        tl.right(5)
        leaf_up(size - 1, angle, times - 1) # Рекурсия

def leaf_down(size, angle, times):
    """
    Построение нижней части листа
    """
    if times > 0:
        tl.left(180 - angle)
        tl.forward(size - 20)
        tl.left(angle + 2.5)
        tl.forward(size - 35)
        tl.right(175)
        leaf_down(size - 1, angle, times - 1) # Рекурсия

def leaves(size, angle, n_leaves):
    """
    Построение всех листьев
    """
    if n_leaves > 0:
        tl.color('black', 'green')
        tl.begin_fill()
        heading = tl.heading()
        x0, y0 = tl.xcor(), tl.ycor()
        leaf_up(size, angle, 11)
        x1, y1 = tl.xcor(), tl.ycor()
        tl.penup()
        tl.goto(x0, y0)
        tl.pendown()
        tl.setheading(heading)
        leaf_down(size, angle, 11)
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

def palm(size, angle, n_leaves):
    """
    Построение всей пальмы
    """
    trunk(size)
    node = (tl.xcor() + 10, tl.ycor())
    tl.penup()
    tl.left(75)
    tl.backward(75)
    tl.pendown()
    coconuts(size)
    tl.goto(node)
    tl.left(21)
    leaves(size, angle, n_leaves)

"""
Приготовление к выполнению фунций
"""
tl.delay(0) 
tl.speed(100)
tl.penup()
tl.goto(40,-320)
tl.pendown()

"""
Эти переменные нельзя изменять, данные значения нужны для корректной работы функций (и упрощения их написания)
"""
size = 80
angle = 162
n_leaves = 5

palm(size, angle, n_leaves)

tl.done()
