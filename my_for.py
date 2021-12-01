def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			func(next(iterator))
		except StopIteration:
			break


my_for("hello", print)