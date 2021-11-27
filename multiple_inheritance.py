class Aquatic:
	def __init__(self, name):
		self.name = name

	def swim(self):
		return f"{self.name} is swimming."

	def greet(self):
		return f"I am {self.name} of the sea!"


class Ambulatory:
	def __init__(self, name):
		self.name = name

	def walk(self):
		return f"{self.name} is walking."

	def greet(self):
		return f"I am {self.name} od the land!"


class Pinguin(Ambulatory, Aquatic):
	def __init__(self, name):
		super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Pinguin("Captain Cook")

print(jaws.swim())
print(lassie.name)
print(captain_cook.greet())

