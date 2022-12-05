import random

def Create_Random(k):
    st = ''
    while k > 0:
        r = random.randint(0, 100)
        if k == 1:
            st += str(r) + '*x' + ' + '
        else:
            st += str(r) + '*x' + str(k) + ' + '
        k -= 1
    st += str(random.randint(0, 100))
    return st

def Create(k, lis):
    st = ''
    count = 0
    while k > 0:
        if k == 1:
            st += str(lis[count]) + '*x' + ' + '
        else:
            st += str(lis[count]) + '*x' + str(k) + ' + '
        k -= 1
        count += 1
    st += str(lis[-1])
    return st

def Clear(st):
    lis = []
    for i in st:
        temp_st = ''
        for j in i:
            if j == '*':
                break
            temp_st += j
        lis.append(int(temp_st))
    return lis

k = abs(int(input('Введите число: ')))
st = Create_Random(k)
print(st)
data = open('file1.txt', 'w')
data.writelines(st)
data.close()

flag = int(input('Если хотите создать еще одно множество нажмите 1, если нет то 0: '))
if flag:
    k = abs(int(input('Введите число: ')))
    st = Create_Random(k)
    print(st)
    data = open('file2.txt', 'w')
    data.writelines(st)
    data.close()

flag = int(input('Если хотите сложить эти множества введите 1, если нет то 0: '))
if flag:
    data = open('file1.txt')
    st1 = data.read().split(' + ')
    data.close()
    data = open('file2.txt')
    st2 = data.read().split(' + ')
    data.close()
    lis1 = Clear(st1)
    lis2 = Clear(st2)
    lis3 = []
    if len(lis1) == len(lis2):

        for i in range(len(lis1)):

            lis3.append(lis1[i] + lis2[i])

        k = len(lis1) - 1
        result_str = Create(k, lis3)
    else:
        if len(lis1) < len(lis2):
            lis1, lis2 = lis2, lis1

        temp_list = lis1[-len(lis2):]

        for i in range(len(temp_list)):

            lis3.append(temp_list[i] + lis2[i])

        result_list = lis1[:-len(lis2)] + lis3
        k = len(result_list) - 1
        result_str = Create(k, result_list)

    print(result_str)


