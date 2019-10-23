def isIn(char, aStr):
    """
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr; False otherwise
    """

    def binary_search(aStr,low, high, char):
        if high > low:
            ans = (high + low) // 2
            if char == aStr[ans]:
                return True
            elif char < aStr[ans]:
                return binary_search(aStr, low, ans, char)

            else:
                return binary_search(aStr, ans, high, char)
        else:
            return False

    return binary_search(aStr, 0, len(aStr), char)


print(isIn('j', 'abcdefghiklmnopqrstuvw'))


"""
    low = 0
    high = len(aStr)
    ans = (high + low) // 2
    found_it = False
    epsilon = 0

    while ans > epsilon:

        if char < aStr[ans]:
            high = ans
        elif char > aStr[ans]:
            low = ans
        ans = (high + low) // 2
        if char == aStr[ans]:
            found_it = True
    return found_it
"""
