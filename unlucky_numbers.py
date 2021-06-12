for n in range(1, 21):
	if n == 4 or n == 13:
		print(f"{n} is UNLUCKY!!!")
	elif n % 2 == 0:
			print(f"{n} is even.")
	elif n % 2 == 1:
			print(f"{n} is odd.")