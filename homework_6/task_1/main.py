li = [int(i) for i in input('Введите целые числа через пробел: ').split()]
result = filter(lambda x: 9 < x < 100, li)
print(*result)
