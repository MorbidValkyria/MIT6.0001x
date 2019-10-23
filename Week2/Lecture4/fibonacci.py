def fib(x):
    """
        assumes x an int >= 0:
        returns Fibonacci of x:

    """
    if x == 0 or x == 1:
        return 1
    else:
        # return fib(x-1) + fib(x - 2)

        return round(1.618*fib(x-1))  # Example using the golden ratio


print(fib(8))
