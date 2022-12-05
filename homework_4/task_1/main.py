from math import pi
d = abs(int(input('Введите колличество знаков после запятой до которых вы хотите округлить число Пи: ')))
if d > 0:
    temp = int('1' + '0' * d)
    result = int(pi * temp) / temp
    print(result)
else:
    print(int(pi))
