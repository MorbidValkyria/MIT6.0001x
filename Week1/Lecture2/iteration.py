"""
Square by repetitive addition

"""

x = 3
ans = 0
itersLeft = x

while itersLeft != 0:
    # What this loop does is pretty simple, just makes successive sums and stores the result in ans
    # This way we can square any number n * n also represented as  n**2
    ans += x
    itersLeft -= 1

print(str(x) + "*" + str(x) + " = " + str(ans))
