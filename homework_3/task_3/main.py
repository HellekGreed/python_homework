import math

li = [float(i) for i in input('Введите вещественные чился через пробел: ').split()]
tem = []
for i in li:
    if i == int(i):
        continue
    tem.append(i - int(i))

print(round(max(tem) - min(tem), 2))
