li = [s for s in input('Введите буквы и цифры через пробел: ').split()]
dig_result = filter(lambda x: x.isdigit(), li)
str_result = filter(lambda x: x.isalpha(), li)
print(*dig_result)
print(*str_result)
