first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для first_result
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для second_result
second_result = (len(first[i]) != len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f[0]) - len(f[1]) for f in zip(first, second) if len(f[0]) != len(f[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))