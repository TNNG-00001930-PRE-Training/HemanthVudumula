'''
8. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

upper = lower = 0

for ch in input("Enter the string : "):
	if ch.isalpha():
		if ch.isupper():
			upper += 1
		else : lower += 1

print("Upper", upper, "\nLower", lower)