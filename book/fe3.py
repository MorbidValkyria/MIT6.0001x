current_biggest_int = 0
overall_biggest = 0 

for i in range(0, 6):
    first_integer = int(input("Enter an integer:\n"))
    second_integer = int(input("Enter another integer\n"))
    if first_integer % 2 != 0 and second_integer % 2 != 0:
        if first_integer >= second_integer:
            current_biggest_int = first_integer
        else:
            current_biggest_int = second_integer
    elif first_integer % 2 != 0:
        current_biggest_int = first_integer
    elif second_integer % 2 != 0:
        current_biggest_int = second_integer
    else:
        current_biggest_int = 0
    if current_biggest_int > overall_biggest:
        overall_biggest = current_biggest_int
if overall_biggest == 0:
    print("No odd numbers were entered")
else:
    print("Biggest odd number:{}".format(overall_biggest))
