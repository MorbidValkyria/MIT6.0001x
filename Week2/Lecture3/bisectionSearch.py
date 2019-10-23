x = 25  # our root
epsilon = 0.01  # how close I want to be from the answer
numGuesses = 0  # keep tracks of the number of times we iterated through the loop
# low and high will be the range in which we are gonna look for the square root
low = 1.0
high = x
ans = (high + low) / 2.0  # We make a first guess, which we call the mid point

while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, 'hi =', high, 'ans =', ans)
    numGuesses += 1
    # if answer is too small
    if ans ** 2 < x:
        # change the low range
        low = ans
    # if answer is too big
    else:
        # change the high range
        high = ans
    # in here we take another guess
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
