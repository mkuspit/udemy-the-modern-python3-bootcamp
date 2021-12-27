def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper

def greet():
	print("My name is Michal.")

greetings = be_polite(greet)

greetings()
greetings()
greetings()



def rage():
	print("I HATE YOU!!!")

polite_rage = be_polite(rage)
polite_rage()


### The same with decorators

def be_impolite(fn):
	def wrapper():
		print("Hello w**ker!")
		fn()
		print("F**k off!")
	return wrapper

@be_impolite
def dis():
	print("My name is Mike.")

dis()
dis()