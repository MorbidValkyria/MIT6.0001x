"""
    Strings
"""
hi = "hello there"
print(hi)
# We can also use single quotes
hi = 'hello there'
foo = "This isn't right"
name = "eric"
print(name)
greet = hi + name
print(greet)
greetings = "hello"
# We can concatenate strings which means we can add two strings together
# We can say that the + operator is overloaded
# That means the + operator has a different meaning when working with numbers
greeting = hi + " " + name

# We can also use the * operator
print(3*"eric")

# We can get the length of a string
print(len("eric"))

# The len function also counts spaces, numbers and other characters
print(len("hi there"))
print(len("The bird wasn't home"))
print(len("1234 567 890"))

"""
    Indexing: We can get pieces or substrings from a string
"""

print("eric"[1])  # returns r
# why does it returns r? Because when indexing programming languages count from 0
"""
    | e | r | i | c |
    | 0 | 1 | 2 | 3 |
    
    - As you can see, when indexing programming languages start counting from 0, but len function counts from 1
"""

# So if we want the first character from the string we have to ask for the char at the 0's place
print("eric"[0])  # Now returns e

# We can do the same with variables
print(name[0])

# If we go out of bounds and ask for a value over the number of characters it has it will throw an error
print(name[4])  # Since we start counting from 0, then the limit on this string would be 3.
# The limit will always be len(string)-1


# Now we can index more than 1 character
print("eric"[1:3])  # The way this works is [start : ending]  and works as [x, n-1]

print("eric"[:3])



