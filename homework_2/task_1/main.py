def fact(num):
    if num == 1:
        return 1
    return num * fact(num - 1)

n = int(input('Введите число: '))
result = list()

for i in range(1, n + 1):
    result.append(fact(i))

print(result)
