def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

print(count_up_to(5))

counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))

for n in counter:
    print(n)