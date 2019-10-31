"""
Finger exercise: Write a program that asks the user to enter an integer and
prints two integers, root and pwr , such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect.
"""

userInput = int(input("Enter a number: "))
foundIt = False
root = 0
while not foundIt:
    root += 1
    for pwr in range(1, 6):
        if root**pwr == userInput:
            foundIt = True
            break
    if root > userInput:
        break

if not foundIt:
    print("Haven't found an answer")

else:
    print(f"{root}**{pwr}={userInput}")
