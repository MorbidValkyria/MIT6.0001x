def func_a():
    """
    This functions takes no parameters and just prints something to the screen
    :return: None
    """
    print("Inside func_a")


def func_b(y):
    """
    This function takes one param y
    :param y: Takes any input
    :return: Returns the same input
    """
    print("Inside func_b")
    return y


def func_c(z):
    """

    :param z: Takes a function
    :return: function z
    """
    print("Inside func_c")
    return z()


print(func_a())
print(5 + func_b(2))
print(func_c(func_a()))

