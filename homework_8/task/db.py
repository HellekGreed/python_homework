
def db_save(name, data):
    with open(f'{name}.txt', 'w') as file:
        for key, val in data.items():
            file.write('{}:{}\n'.format(key, val))

def db_read(name):
    d2 = {}
    with open(f'{name}.txt') as file:
        for i in file.readlines():
            key, val = i.strip().split(':')
            d2[key] = val

    return d2
