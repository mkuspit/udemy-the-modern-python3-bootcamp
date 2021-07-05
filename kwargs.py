def my_fun_1(**kwargs):
	print(kwargs)
my_fun_1(one=1, two=2, three=3)

def my_fun_2(**kwargs):
	print(kwargs.keys())
my_fun_2(one=1, two=2, three=3)

def my_fun_3(**kwargs):
	for name, number in kwargs.items():
		print(f"{name} is numeric {number}")
my_fun_3(one=1, two=2, three=3)