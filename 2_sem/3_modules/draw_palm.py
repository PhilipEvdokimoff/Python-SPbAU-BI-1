import turtle as tl
import palm


def draw_palm(size, angle, n_leaves):
    """
    Приготовление к выполнению фунций
    """
    tl.delay(0) 
    tl.speed(100)
    tl.penup()
    tl.goto(40,-320)
    tl.pendown()

    palm.palm(size, angle, n_leaves)  # !!! ИСПОЛЬЗОВАН МОДУЛЬ !!!

    tl.done()
