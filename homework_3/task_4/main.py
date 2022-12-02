num = int(input('Введите целое число: '))
result = ''
while num > 0:
    result += str(num % 2)
    num //= 2
print(result[::-1])
