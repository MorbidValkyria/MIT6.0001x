"""
    Find cube roots using  guess and check algorithms

"""

x = int(input("Enter an integer: "))
ans = 0
while ans**3 < x:
    # since ans starts at 0, we will increment it by one each time it loops until it reaches an answer or
    # goes over the answer
    ans += 1

# If ans to the power of 3 does not equal or number, then it's not a perfect cube
if ans**3 != x:
    print(str(x) + " is not a perfect cube")
else:
    print("Cube root of " + str(x) + " is " + str(ans))

"""
    Modification of the above code so it can work with negative inputs
"""

x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):  # this time we are checking with abs so we can work with negative numbers
    ans += 1
if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans))

"""
    Cleaning up 
"""

cube = 13
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(str(cube) + " is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))
