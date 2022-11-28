n = int(input('Введите число N(оно должно быть больше 1): '))
lis = [i for i in range(-n, n + 1)]
print('Введите по очереди 5 индексов чисел из списка которые хотите перемножить(Индекс не может быть больше чем N * 2).')
index = [abs(int(input())) for _ in range(5)]
result = 1
for i in index:
    result *= lis[i]
print(result)
