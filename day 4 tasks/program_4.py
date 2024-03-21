'''
4. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class Str:
	text = ""
	def __init__(self, text = None):
		self.text = text
	def getString(self):
		self.text = input("Enter the text : ")
	def printString(self, testing = False):
		if testing == True:
			return self.text.upper()
		else:
			print(self.text.upper())


def testing(text = "hello"):
	test = Str(text)
	if text.upper() == test.printString(True):
		print("working sucessfully")
	else :
		print("not working properly")
'''
st = Str()
st.getString()
st.printString()
'''

testing()





