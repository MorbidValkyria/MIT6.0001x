s = "abcdefgh"
for index in range(len(s)):
	if s[index] == "i" or s[index] == "u":
		print("There is an i or u")


# Code can be rewrited as 

for char in s:
	if char == "i" or char == "u":
		print("There is an i or u")