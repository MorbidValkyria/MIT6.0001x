"""
Comparisons

"""

print(2 < 3)  # Returns True as 3 is bigger than 2
print(2.0 > 3.0)  # Returns False as 2.0 is not gigger than 3.0
print(2 <= 2)  # Returns True as 2 equals 2
print(2 < 2)  # Returns False as 2 is not less than 2
print(2 == 2)  # Returns True as 2 equals 2
print(2 != 2)  # Returns False as 2 does equal to 2

"""
    Even or Odd??
"""

x = int(input("Enter an integer: "))

if x % 2 == 0:  # Test
    # True block
    # All indented code inside the if clause belongs to this block of code
    print("")
    print("Even")


else:  # if the above condition isn't satisfied this gets executed
    # False block
    print("")
    print("Odd")

print("Done with conditional")

"""
    Nested conditionals!
    - By nesting we mean conditionals inside other conditionals
"""

x = 20

if x % 2 == 0:
    # We can nest conditionals inside other conditionals
    if x % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2")
elif x % 3 == 0:  # Short for else if, if the last condition returned False, then see if this is truth.
    print("Divisible by 3")
else:
    print("Not divisible by 2 and 3")

"""
    Compound booleans
"""

x = 3
y = 4
z = 0
if x < y and x < z:  # Combination of boolean comparisons using and
    print("x is least")
elif y < z:  # Short for else if, if the last condition returned False, then see if this is truth.
    print("y is least")
else:
    print("z is least")

"""
    Indentation:
    -Indentation is basically the tabs or whitespace before a logical expression.
    -When we indent, we group statements to form blocks of code
    -For now we use them to group code in conditionals, but later you will learn other uses
"""

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:  # Remember we always use == for comparisons as = is for assignment.
    print("x and y are equal")
    if y != 0:
        print("Therefore x / y is ", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("Thanks!")
