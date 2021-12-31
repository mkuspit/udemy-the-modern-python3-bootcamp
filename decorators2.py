def shout(fn):
	def wrapper(*args, **kwargs):
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}."


@shout
def order(main, side):
	return f"I'd like the {main} with a side of {side}, please."

@shout
def lol():
	return "lol!"

print(greet("Mike"))

print(order("steak", "fries"))