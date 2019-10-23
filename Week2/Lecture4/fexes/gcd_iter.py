def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = max(a, b)
    biggest = 1

    for i in range(1, x + 1):
        if a % i == 0 and b % i == 0:
            biggest = i
    return biggest

print(gcdIter(17, 12))