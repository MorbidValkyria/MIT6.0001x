import math as mt


def polysum(n, s):
    """
    :param n: number of sides
    :param s: length of the sides
    :return: The sum of the area and the square of the perimeter

    """
    return round((0.25 * n * s ** 2 / mt.tan(mt.pi / n)) + (n * s) ** 2, 4)
