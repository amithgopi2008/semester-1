import math

def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    return (mid_x, mid_y)


def length(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance