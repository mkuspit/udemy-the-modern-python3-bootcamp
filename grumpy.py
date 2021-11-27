class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f" {key} is not here!")

data = GrumpyDict({'first': 'Tom', 'animal': 'cat'})
print(data)