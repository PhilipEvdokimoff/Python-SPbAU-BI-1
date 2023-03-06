import turtle as tl


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
