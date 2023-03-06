import turtle as tl


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
