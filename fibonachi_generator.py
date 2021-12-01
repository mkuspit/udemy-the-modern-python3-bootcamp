def fibonachi_generator(max, a = 0, b = 1):
	count = 0
	while count < max:
		a, b = b, a + b
		yield a
		count += 1

for n in fibonachi_generator(5):
	print(n)

fib_list = list(fibonachi_generator(10))
print(fib_list)