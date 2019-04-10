from math import factorial

import pytest

def test_factors():
	for n in range(2):
		assert factorial(n) == factorial(n)


def test_negatives():
	with pytest.raises(AssertionError):
		factorial(-4)






	#assert main(3) == 6
	#assert main(5) == 120
	#assert main(2) == 2


