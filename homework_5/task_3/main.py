def encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char

        else:
            decode += char * int(count)
            count = ''
    return decode


strin = input('Введите строку которую хотите закодировать: ')
result = encode(strin)
data = open('encode.txt', 'w')
data.writelines(result)
data.close()
print(f'Результат кодирования:\n{result}')

flag = int(input('Хотите ли раскодировать содержимое файла "encode.txt":\n1 - ДА\nЛюбая другая кнопка - Нет\n'))
if flag == 1:
    data = open('encode.txt').read()
    print(f'Содержимое файла:\n {data}')
    deco = decode(data)
    print(f'Результат декодирования\n{deco}')
    data = open('decode.txt', 'w')
    data.writelines(deco)
    data.close()



