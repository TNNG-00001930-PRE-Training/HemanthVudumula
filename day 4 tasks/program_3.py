'''
3. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''

inp_str = input("Enter the comma seperated string : ")

val = inp_str.split(',')
lis = list(val)
tup = tuple(val)
print(lis)
print(tup)