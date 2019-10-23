cube = 27
epsilon = 0.01 #The larger epsilon is, we will be far away from the answer to a point we might miss it
guess = 0.0
increment = 0.00001 #The smaller the increment value is the closer the guess will be but the slower the program will be

numOfGuesses = 0 # To keep track each time we iterare through the loop

while abs(guess**3 - cube) >= epsilon and guess <= cube:
	guess += increment
	numOfGuesses += 1

print("number of guesses:", numOfGuesses)
if abs(guess**3 - cube) >= epsilon:
	print("Failed on cube root of", cube)
else:
	print(guess, "is close enough to cube root of", cube)
