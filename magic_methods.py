class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def __repr__(self):
		return f"Human named {self.first} {self.last}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		if isinstance(other, Human):
			return Human("Newborn", self.last, 0)
		return "You can't add that"



j = Human("Jenny", "Larson", 27)
print(j)
print(len(j))

k = Human("Kevin", "Jones", 30)

print(j+k)