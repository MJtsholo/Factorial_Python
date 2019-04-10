
n = eval(input("Please enter a whole number: "))
fact = 1

def factorial():
	global fact
	global n
	if n < 0:
		print("Sorry, factorial does not exist for negative numbers")
	elif n == 0:
	   print("The factorial of 0 is 1")
	else:
	   for n in range(1,n + 1):
	       fact = fact * n
	   print("The factorial of",n, "is ",fact)
	
def not_number():
	while True:
		try:
			n = eval(input("Please enter a whole number: "))
			if type(n) == int :
				return ValueError
		except ValueError:
			print('That is not a number!')

factorial()
not_number()		




if __name__ == '__main__':
	factors.factorial()