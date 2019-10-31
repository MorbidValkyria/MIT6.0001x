"""
Finger exercise: Write a program that examines three variables— x , y , and z —
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect

"""

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
z = int(input("Enter the value for z: "))
biggest = 0 # The variable that will hold the biggest odd number

### There are a couple of ways to solve this, I'll show the one I think it's easier to understand

############# First we check if all 3 numbers are odd and search for the biggest #############
if x % 2 != 0 and z % 2 != 0 and y % 2 != 0:
	if x >= y and x >= z:
		biggest = x
	elif y >= z and y > x: # Over here we don't have to check if y is equal to x, because we already tested for that
		biggest = y
	else:
		biggest = z

############# Now we check if x and either y or z is odd #############

elif x % 2 != 0:
	if y % 2 != 0:
		if x >= y:
			biggest = x
		else:
			biggest = y
	elif z % 2 != 0:
		if x >= z:
			biggest = x
		else:
			biggest = z
	else:
		biggest = x

############# Now we check if y is odd or z #############

elif y % 2 != 0:
	# We already know that x is not odd so we only check for z
	if z % 2 != 0:
		if y >= z:
			biggest = y
		else:
			biggest = z
	else:
		biggest = y
############# Now we check if z is odd #############
elif z % 2 != 0:
	biggest = z

else:
	print("No odd numbers were entered")

if biggest > 0:
	print(f"Biggest odd number is {biggest}")









