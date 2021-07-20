midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['jan', 'tom', 'dan']



final_grades_1 = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades_1)

final_grades_2 = dict(
	zip(
		students, 
		map(lambda pair: max(pair), zip(midterms, finals))
	)
)
print(final_grades_2)