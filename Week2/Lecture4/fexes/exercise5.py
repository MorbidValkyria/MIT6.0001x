"""
    1)
"""


def foo(x, y=5):

    def bar(x):
        return x + 1

    return bar(y * 2)


foo(3)

# Answer: 11

"""
    2)
"""
def foo(x, y=5):
    def bar(x):
        return x + 1

    return bar(y * 2)


foo(3, 0)

# Answer: 1

"""
    3)
"""


def foo(x):
    def bar(z, x=0):
        return z + x

    return bar(3, x)


foo(2)

# Answer: 5

"""
    4)
"""

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)

# Answer: 3


