li = [int(i) for i in input('Введите целые числа через пробел: ').split()]
result = []
if len(li) % 2 == 0:
    for i in range(int(len(li) / 2)):
        result.append(li[i] * li[-(i + 1)])
else:
    for i in range(int((len(li) - 1) / 2) + 1):
        result.append(li[i] * li[-(i + 1)])
print(result)

