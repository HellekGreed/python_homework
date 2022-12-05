n = abs(int(input('Введите число: ')))
lis = []
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        lis.append(i)
count = 0
while n > 1:
    if n % lis[count] == 0:
        n = n / lis[count]
        print(lis[count], end=' ')
    else:
        count += 1
    
