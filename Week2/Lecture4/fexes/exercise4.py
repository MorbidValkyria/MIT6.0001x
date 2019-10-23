"""
Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated.
If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the result is a
function, select function and write 'function' in the box.
"""

a = 10


def f(x):
    """
    :param x: Num type
    :return: Sum of two numbers
    """
    return x + a


a = 3
print(f(1))

# answer: int, 4.
# Why 4 is returned instead of 11? because we changed the value of a before the function call.

x = 12


def g(x):
    """
    :param x: any number
    :return: function h
    """
    x = x + 1

    def h(y):
        """
        :param y: Any number
        :return: Sum of two numbers
        """
        return x + y

    return h(6)


print(g(x))

# answer: int, 19.

