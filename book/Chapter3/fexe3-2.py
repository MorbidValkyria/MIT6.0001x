
"""

Finger exercise: Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g., s = '1.23,2.4,3.123' . Write a program that prints
the sum of the numbers in s.

"""

s = '1.23,2.4,3.123'  # Will only work with sample in this format.
n = ''
mySum = 0
for i in range(len(s)):
    if s[i] != ',':
        n += s[i]
    if s[i] == ',' or i == len(s) - 1:
        mySum += float(n)
        n = ''

print(mySum)
