import sys
def factorial(numbers):
	try:
		numbers = int(numbers)
	except:
		print("That is not a number!")
		return "That is not a number!"

	if numbers > -1:
		fact = 1
		if numbers == 0:
			print("1")
			return 1
		else:
			while numbers >= 1:
			 	fact = fact * numbers
			 	numbers = numbers - 1
			print(fact)
			return fact
	else:
		print("False")
		return False



if __name__ == '__main__':
	numbers = input("Please enter number: ")
	factorial(numbers)