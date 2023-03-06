import turtle as tl


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
