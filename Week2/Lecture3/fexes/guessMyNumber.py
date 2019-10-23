print("Please think of a number between 0 and 100!")

high = 100
low = 0

guess = False

while not guess:
    answer = (high + low) // 2
    print("Is your secret number {}?".format(answer))
    user_answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter\
     'c' to indicate I guessed correctly.")
    if user_answer == "h":
        high = answer
    elif user_answer == "l":
        low = answer
    elif user_answer == "c":
        guess = True
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: {}".format(answer))
