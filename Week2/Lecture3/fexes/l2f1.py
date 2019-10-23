
# 1)

iteration = 0
count = 0
while iteration < 5: #will iterate 5 times from 0 to 4
    # the variable 'letter' in the loop stands for every 
    # character on the string, including spaces and commas!
    for letter in "hello, world": 
        count += 1 #For each character in "hello, world" count will be incremented by 1(includes the coma and white space)
    print("Iteration " + str(iteration) + "; count is: " + str(count)) # prints the current iteration and the value of count
    iteration += 1 #Each iteration the variable iteration will be incremented by 1

"""
Answers:
	 1) What is the value of the variable count that is printed out (at the print statement) on iteration 0? 
	 	12

	 2)What is the value of the variable count that is printed out (at the print statement) on iteration 1? 
	 	24

	 3)What is the value of the variable count that is printed out (at the print statement) on iteration 2? 
	 	36

	 4)What is the value of the variable count that is printed out (at the print statement) on iteration 3? 
	 	42

	 5)What is the value of the variable count that is printed out (at the print statement) on iteration 4?
	 	60
Explanation:
	This exercise it's pretty easy to understand even without running the code. 
	
	First we set the variables of iteration and count to 0. Iteration will keep track of the times we iterate through
	the loop and count will be used to store the number of characters in "hello, world"

	Now we encounter a while loop, while iteration is less than 5. Remember we set the variable iteration to 0? Now
	inside the while loop we encounter another loop, a for loop, this one will loop through each character in 
	"hello, world" and store the number in count, counting not just letters but also comas and white space. The 
	number of characters will be 12. 

	After that we get a print function that will print the current iteration and the value inside count during that iteration.

	Finally we have the variable iteration been incremented by 1, we can infer from this that the while loop will iterate a total
	of 5 times (0, 1, 2, 3, 4)

	We have all the information we need to solve the questions without even running the code.
	During iteration 0 the value of count will be 12 * 1
	During iteration 1 the value of count will be 12 * 2
	During iteration 2 the value of count will be 12 * 3
	During iteration 3 the value of count will be 12 * 4
	During iteration 4 the value of count will be 12 * 5
"""

# 2)

iteration = 0 
while iteration < 5:
	# notice how we initialize count inside the loop this time
	# we will see the changes this has to the code
    count = 0 
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

"""
Answers:
	1) What is the value of the variable count that is printed out (at the print statement) on iteration 0? 
		12
	2) What is the value of the variable count that is printed out (at the print statement) on iteration 1? 
		12
	3) What is the value of the variable count that is printed out (at the print statement) on iteration 2? 
		12
	4) What is the value of the variable count that is printed out (at the print statement) on iteration 3?
		12
	5) What is the value of the variable count that is printed out (at the print statement) on iteration 4?
		12

Explanation:
	If the last one was easy, this one is even easier. The exercise is exactly the same as before only with one
	change, the variable of count it's been declared inside the while loop. This means each time we iterate the last value
	of count will be overwritten and reset to 0. Unlike last time when each iteration the value of count retained the previous
	value and incremented by 12. That's why each iteration the value of count will stay the same.   


"""

# 3)

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        # Same code as ex 2, but this little if statement gets added
        # if the reminder of dividing the value of iteration and 2 is 0
        # then it will break out of the for loop
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


"""
Answers:
	1) How many times will the print statement be executed? 
		5
	2) What is the largest value of the variable iteration that will be printed out (at the print statement)? 
		4
	3) What is the largest value of the variable count that will be printed out (at the print statement)? 
		12
	4) What is the smallest value of the variable count that will be printed out (at the print statement)? 
		1


Explanation:
	The code might look complicated but it isn't. It's pretty much the same as last exercise, but with one small 
	addition, each time iteration % 2 == 0, the break statement will kick in and count will only be incremented by one.

Output of the code:
Iteration 0; count is: 1
Iteration 1; count is: 12
Iteration 2; count is: 1
Iteration 3; count is: 12
Iteration 4; count is: 1

"""