first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zipped = list(zip(first,second))
first_result = (len(x[0])-len(x[1]) for x in zipped if len(x[0]) != len(x[1]))
second_result = (len(first[x]) == len(second[y]) for x in range(len(first)) for y in range(len(second)) if x == y)

print(list(first_result))
print(list(second_result))