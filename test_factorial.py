
from factorial import factorial
import pytest

def test_factors():
	result = factorial(3)
	assert result == 6

	result = factorial(5)
	assert result == 120

	result = factorial(-2)
	assert result == False

	result = factorial(0)
	assert result == 1

	result = factorial("c")
	assert result == "That is not a number!"

	result = factorial("H")
	assert result == "That is not a number!"

	result = factorial("")
	assert result == "That is not a number!"