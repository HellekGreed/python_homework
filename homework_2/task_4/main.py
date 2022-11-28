n = abs(int(input('Введите целое число: ')))
result = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        result += i
print(f"Сумма всех четных чисел от 1 до {n}: {result}")
