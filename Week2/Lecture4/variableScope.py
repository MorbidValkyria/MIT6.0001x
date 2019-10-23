def f(x):
    """

    :param x: int or float
    :return: int or float
    """
    x += 1
    print("in f(x) x = x".format(x))
    return x


x = 3
z = f()
print(z)
