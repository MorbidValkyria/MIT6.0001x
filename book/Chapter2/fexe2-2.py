"""
Finger exercise: Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.

"""

# My thought process lies in using a for loop, looping 5 times 
# and asking for two integers each loop, we will compare both of them
# saving the current largest and the overall largest odd number

current_largest = 0
largest_odd = 0

for i in range(0,5):
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))
    if x % 2 != 0 and y % 2 != 0:
        if x >= y:
            current_largest = x
        else:
            current_largest = y
    elif x % 2 != 0:
        current_largest = x
    elif y % 2 != 0:
        current_largest = y
    else:
        current_largest = 0

    if current_largest >= largest_odd:
        largest_odd = current_largest

if largest_odd > 0:
    print(f"Largest odd number: {largest_odd}")
else:
    print("No odd numbers were entered!")



















