def isPalindrome(s):
    """
        Checks if a string is a palindrome
    """

    def toChar(s):
        """
        :param s: Takes a string for input
        :return: Returns the string stripped of spaces and all chars converted to lower case
        """
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghikjlmnopqrstuvwxyz":
                ans += c
        return ans

    def isPal(s):
        """
        :param s: Takes a string for input, string can be empty
        :return: Returns True if the string is a palindrome or if the string is empty
        """
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1: -1])
    return isPal(toChar(s))

print(isPalindrome("Abba Abba"))