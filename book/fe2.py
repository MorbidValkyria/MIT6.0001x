"""
Finger exercise: Write a program that examines three variables— x , y , and z —
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect.
"""

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))

if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    if x >= y and x >= z:
        print("Biggest odd number is", x)
    elif y >= x and y >= z:
        print("Biggest odd number is", y)
    else:
        print("Biggest odd number is", z)
elif x % 2 != 0:
    if y % 2 != 0:
        if x >= y:
            print("Biggest odd number is", x)
        else:
            print("Biggest odd number is", y)
    elif z % 2 != 0:
        if x >= z:
            print("Biggest odd number is", x)
        else:
            print("Biggest odd number is", z)
    else:
        print("Biggest odd number is", x)
elif y % 2 != 0:
    if z % 2 != 0:
        if y >= z:
            print("Biggest odd number is", y)
        else:
            print("Biggest odd number is", z)
    else:
        print("Biggest odd number is", y)
elif z % 2 != 0:
    print("Biggest odd number is", z)
else:
    print("No odd numbers were entered!")
