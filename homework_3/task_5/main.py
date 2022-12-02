n = int(input('Введите целое число: '))
a, b = 1, 1
lis1 = [0, 1]
lis2 = [1,]
for i in range(n - 1):
    lis1.append(b)
    if i % 2 == 0:
        lis2.append(-b)
    else:
        lis2.append(b)
    a, b = b, a + b
result = lis2[::-1] + lis1
print(result)
