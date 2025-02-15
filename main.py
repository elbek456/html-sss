lst = [1, 3.4, 'salom', 23, 3.6]
numbers_count=0
for i in lst:
    if isinstance(i, int):
        numbers_count += 1


print(numbers_count)