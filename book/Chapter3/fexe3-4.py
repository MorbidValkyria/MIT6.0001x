"""
Finger exercise: What would have to be changed to make the code in Figure
3.4 work for finding an approximation to the cube root of both negative and
positive numbers? (Hint: think about changing low to ensure that the answer
lies within the region being searched.)
"""

# Code in question:
x = -25
epsilon = 0.01
numGuesses = 0
low = min(x, 0.0)  ## Part we fixed 
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
