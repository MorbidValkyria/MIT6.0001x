n = input("You're in the Lost Forest. Go left or right?\n")
while n == "right":  # As long as the user enters right, the loop will keep rolling
    n = input("You're in the Lost Forest. Go left or right?\n")
print("You're out of the Lost Forest")

# more complicated with while loops
n = 0

while n < 5:
    print(n)
    n += 1
"""
    We get the following output:
     - 0
     - 1
     - 2
     - 3
     - 4
    Why didn't the 5 get printed out? Because print is inside the while loop, and underneath  is the increment variable
    so once the condition is 5 < 5, it returns False so it isn't execute.
"""

# Now try switching the increment variable before the print function
n = 0
while n < 5:
    n += 1
    print(n)

"""
    Notice the following output:
        - 1
        - 2
        - 3
        - 4
        - 5
    Since the increment variable happens before the print statement now 5 get's printed but 0 get's left out
"""

# shortcut with for loop
# As you can see for loops work a little bit different than while loops
# the n get's initialize in the for loop
# Range will return the integers from 0 until one number, in this case range(5) will return numbers 0-4
# That means n will hold the values of 0, 1, 2, 3, 4 respectively to each iteration
for n in range(5):
    print(n)

"""
    range actually has a few other tricks. range works the following ways:
        - range(stop) were range will return the values 0-stop - 1
        - range( start, stop) were range will return the values from start - stop -1
        - range(start, stop, step) were range will return the values start-stop -1 skipping each step size
"""
# uncomment the print statements to check out the value of i during each iteration
mysum = 0

for i in range(7, 10):
    #print("Current value of i:", i)
    mysum += i

print(mysum)

mysum = 0
for i in range(5, 11, 2):
    #print("Current value of i:", i)
    mysum += i

print(mysum)

"""
    break statements: these are used to break out of loops
"""

mysum = 0

for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:  # Once mysum equals to five, the break statement will kick in
        break
print(mysum)  # mysym equals to five because we broke out of the loop

