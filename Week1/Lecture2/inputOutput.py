"""
 String formatting
"""

x = 1
print(x)
x_str = str(x)  # str() will convert the value of x into a string

# We have here a couple of methods we can use to print multiple elements and insert them inside  a string
# First method will be separating elements inside the string with a coma
print('my fav number is', x, '.', 'x =', x)  # This method inserts a space between elements.

# The second method will be using the + operator to concatenate strings
# For this method the elements need to be converted into strings first
# which is why we created the x_str variable, remember this method will not add spaces,
# so you will have to add them in the string
print('my fav number is ' + x_str + '.' + ' x = ' + x_str)

# Third method (not discussed in video lectures) is the % insertion
# Using %i because the value I'm inserting is of type int
print("my fav number is %i. x = %i" % (x, x))

# That means I can use %s for string types
print("my fav number is %s. x = %s" % (x_str, x_str))  # Make sure after % you use i, s, etc matching the variable type
# Fourth method using format()
print("my fav number is {}. x = {}".format(x, x))
# With format you can use numeric values and strings
print("my fav number is {}. x = {}".format(x_str, x_str))
# format has another cool feature
foo = 3
bar = 6
foobar = 9
print("{} {} {}".format(foo, bar, foobar))
print("{2} {0} {1}".format(foo, bar, foobar))  # We can change the order by calling the index directly inside the {}

"""
    Take input from the user
"""
# input will take an argument string, this string will be printed on the string
# normally this string will ask for user input
# and input will return a string ALWAYS, and I will said it again ALWAYS, regardless if user entered a number value
text = input("Type anything... ")
print(5*text)
print(type(text))
# Now we can convert the string that input returns to a numerical value
# Returns an int
num = int(input("Type a number..."))
print(5*num)
print(type(num))
# Also works with floats
myFloat = float(input("Type a number..."))
print(myFloat)
print(myFloat*5)
print(type(myFloat))
