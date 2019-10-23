def print_name(firstName, lastName, reverse=False):
    """
    :param firstName: String first name
    :param lastName:  String last name
    :param reverse:  boolean
    :return: None
    """
    if reverse:
        print(lastName, ',',  firstName)
    else:
        print(firstName, lastName)


print_name("Eric", "Grimson", True)
print_name("Eric", "Grimson", False)
print_name("Eric", "Grimson", reverse=False)  # We can specify a parameter
print_name("Eric", lastName="Grimson", reverse=False)
# If we specify each param, then we can change the order
print_name(lastName="Grimson", reverse=False, firstName="Erick")
print_name("Erick", "Grimson")  # If we specified a param in the function we can ignore that param