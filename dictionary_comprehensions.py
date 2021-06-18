numbers = {'first': 1, 'second': 2, 'third': 3}
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

numbers = [1, 2, 3, 4]
squared_numbers_2 = {num: num**2 for num in numbers}
print(squared_numbers_2)

string_1 = 'ABCD'
string_2 = '1234'
my_dict = {string_1[i]: string_2[i] for i in range(len(string_1))}
print(my_dict)

numbers_2 = list(range(12))
even_odd = {num:('even' if num % 2 == 0 else 'odd') for num in numbers_2}
print(even_odd)