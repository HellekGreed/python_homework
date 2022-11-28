n = int(input('Введите число: '))
result = 1
for i in range(2, n + 1):
    if n % i == 0:
        result = i
        break
print(f'Наименьший делитель числа {n} отличный от 1 это: {result}')
