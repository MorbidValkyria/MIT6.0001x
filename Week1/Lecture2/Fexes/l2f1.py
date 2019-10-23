"""
1) "a" + "bc" -> abc

2) 3 * "bc" -> bcbcbc

3) "3" * "bc" -> error as we can't use the * operator on two strings

4) abcd"[2] -> c (Just takes the character at index 2 in the string. a has index 0 and b index 1)

5) "abcd"[0:2] -> ab (Returns the substring from index 0 all the way to index n -1 in this case b)

6) "abcd"[:2] -> ab (Not giving a starting value to slice the string we start at 0)

7) "abcd"[2:] -> cd (When we don't give an end value it goes all the way to the end of the string)

"""