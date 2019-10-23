# First example
def f(y):
    x = 1
    x += 1
    return x


x = 5
f(x)
print(x)


# Second example

def g(y):
    print(x)
    print(x + 1)


x = 5
g(x)
print(x)

# Third example

def h(y):
    x = x + 1
x = 5
h(x)
print(x)