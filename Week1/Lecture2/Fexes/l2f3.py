#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:26:43 2018

@author: francisco
"""

#1)
if 6 > 7:
   print("Yep")
 
# Answer: Blank

# Since 6 is not greater than 7, it doesn't print anything and it doesn't have any
# more conditionals to evalutate.

#2)
if 6 > 7:
   print("Yep")
else:
   print("Nope")
   
#Answer: Nope

#Same as previous exercise, only this time we have an else statement. So the else statement gets executed.

#3)
var = 'Panda'
if var == "panda":
   print("Cute!")
elif var == "Panda":
   print("Regal!")
else:
   print("Ugly...")

#Answer: Regal!
   
# Strings in Python are case sensitive, the first condition compares 'Panda' with 
# 'panda', thus they're not the same, so we pass on to the next conditional
# this one compares 'Panda' with 'Panda' and they're the same so the code inside
# is executed
   
#4)
temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")

#Answer: Hot
   
# Conditionals are evaluated in order, in this case the first conditions says
# if temp is greater than 85, since it is the conditional ends and the rest
# isn't evaluated. That's why it prints hot and not REALLY HOT!

#5)
temp = 50
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")

# The value of temp is 50 and the 3 conditions compares if temp is greater than
# 85, 100 and 60, 50 is not greater than any of them so each condition returns
# false so the code inside the else statement is the one that gets executed
