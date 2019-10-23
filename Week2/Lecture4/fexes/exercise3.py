"""

Assume the following definitions have been made:
"""


def a(x, y, z):
    """
    :param x: Boolean
    :param y: Any num type
    :param z: Any num type
    :return: Either x o y, both num types
    """
    if x:
        return y
    else:
        return z


def b(q, r):
    """
    :param q: Any num type
    :param r: Any num type
    :return: A function with params q and r
    """
    return a(q > r, q, r)

# a(False, 2, 3) : int, 3

# b(3, 2) : int, 3

# a(3>2, a, b) : function, function

# b(a, b) : NoneType, error
