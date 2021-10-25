class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	# def get_age(self):
	# 	return self._age

	# def set_age(self, new_age):
	# 	self._age = new_age

	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, new_value):
		self._age = new_value

	@property
	def full_name(self):
		return f"{self.first} {self.last}"
	


jane = Human("Jane", "Smith", 45)
print(jane.last)
#print(jane.get_age())
print(jane.age)

jane.age = 23
print(jane.age)
print(jane.full_name)