lis = [int(i) for i in input('Введите числа через пробел: ').split()]
result_list = []
for i in lis:
    if lis.count(i) == 1:
        result_list.append(i)
print('Данные числа встречаются в единственном экземпляре: ')
print(*result_list)
