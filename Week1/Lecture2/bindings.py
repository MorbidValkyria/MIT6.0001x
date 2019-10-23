
"""
    Binding: means storing a value in a variable
"""
x = 2  # We bind the value of 2 to x
x = x * x  # Replaces(overwrites) the value of x with 4, (2 * 2)
y = x + 1  # Binds the value of 4 + 1 to y
print(y)  # Prints 5 to the screen

"""
    Swap values
"""

# The wrong way:
x = 1  # We bind the value of 1 to the variable of x
y = 2  # We bind the value of 2 to the variable of y
y = x  # We overwrite the value of y with the value of x which is 1
x = y  # We overwrite the value of x with the value of y, which is 1. So we didn't really swapped the values.
print(x)  # Prints 1 to the screen
print(y)  # Prints 1 to the screen
# Why is this isn't working? Well once we bind the the value of x to the value of y, it's previous value is lost.
########################################################################
# First way of swapping values
# (common way as it works in other programming languages and considered the right way)
# With a temporary variable
########################################################################

x = 1  # We bind the value of 1 to the variable of x
y = 2  # We bind the value of 2 to the variable of y
temp = y  # We assign the value of y to a temp variable
y = x  # We overwrite the value of y with the value of x which is 1
x = temp  # We overwrite the value of x with the value inside temp
print(x)  # Prints 2
print(y)  # Prints 1

#########################################################################
# Second Way (The Pythonic way but not a very good Way of doing it,
#  as it only works on Python and not other languages
#########################################################################

x = 1
y = 2
x, y = y, x
print(x)
print(y)

