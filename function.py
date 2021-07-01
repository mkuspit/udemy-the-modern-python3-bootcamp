from random import random

def flip_coin():
	random_number = random()
	if random_number < .5:
		return "Heads"
	else:
		return "Tails"

def square(num):
	return num ** 2