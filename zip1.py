list_1 = ['a', 'b', 'c', 'd']
list_2 = [1, 2, 3, 4]

zipped = zip(list_1, list_2)
zipped_list = list(zipped)

zipped = zip(list_1, list_2)
zipped_dict = dict(zipped)

zipped = zip(list_1, list_2)

print(zipped)
print(zipped_list)
print(zipped_dict)