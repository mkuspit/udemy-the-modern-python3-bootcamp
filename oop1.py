class User:
	def __init__(self, user_name, user_age):
		print ("A new user has been created!")
		self.name = user_name
		self.age = user_age


user_1 = User("Mike", 45)
print(user_1.age)

user_2 = User("Dan", 23)
print(user_2.age)