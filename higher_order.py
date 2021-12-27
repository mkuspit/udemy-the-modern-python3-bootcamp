def my_sum(n, func):
	total = 0
	for num in range(n+1):
		total += func(num)
	return total

def square(x):
	return x**2

def cube(x):
	return x**3

print(my_sum(10, square))

print(my_sum(10, cube))