class Pet:
	allowed = ('cat', 'dog', 'rat')
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError("That's not allowed!")
		self.name = name
		self.species = species

cat = Pet("Fluffy", "cat")
