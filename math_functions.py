def add_numbers(a, b):
	return a + b

def subtract_numbers(a, b):
	return a - b
	
def multiply_numbers(a, b):
	return a * b
	
def divide_numbers(a, b):
	return a / b	

def power_numbers(a, b):
	c = a
	while b > 1:
		a = a * c
		b -= 1
	return a

if __name__ == "__main__":
	print("Adding:", add_numbers(2,4))
	print("Subtracting:", subtract_numbers(9,2))
	print("Multiplying:", multiply_numbers(2,3))
	print("Dividing:", divide_numbers(6,3))
	print("Power:", power_numbers(2,3))
	

