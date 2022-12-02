li = [int(i) for i in input('Введите целые числа через пробел: ').split()]
result = 0
for i in range(len(li)):
    if i % 2 != 0:
        result += li[i]
print(result)
