num = input('Введите число: ')
result = sum(list(map(int, filter(lambda x: x.isdigit(), num))))
print(result)
