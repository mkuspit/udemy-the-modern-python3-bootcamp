my_users = [
	{"name":"Adam", "number":4},
    {"name":"Celine", "number":3},
    {"name":"Donald", "number":2},
    {"name":"Burt", "number":1},
]

sorted_users = sorted(my_users, key=lambda user: user['name'])

print(my_users)
print(sorted_users)