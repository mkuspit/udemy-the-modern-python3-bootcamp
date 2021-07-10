my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, my_nums))
print(evens)

odds = list(filter(lambda x: x % 2 != 0, my_nums))
print(odds)