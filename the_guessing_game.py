import random

secret_number = random.randint(1, 10)

guess = None

while guess != secret_number:
	guess = int(input("Pick a number between 1 and 10..."))

	if guess > secret_number:
		print("Too high!")
	elif guess < secret_number:
		print("Too low!")

print(f"Congratulations! {guess} was the secret number!")