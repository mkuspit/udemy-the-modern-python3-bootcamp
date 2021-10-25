class Animal:
	cool = True

	def make_sound(self, sound):
		print(f"This animal says {sound}")

class Cat(Animal):
	pass

blue = Cat()
blue.make_sound("Meow!")

print(isinstance(blue, Cat))
print(isinstance(blue, Animal))