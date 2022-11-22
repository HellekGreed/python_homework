for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            print(f'Для значения предикат ({x},{y},{z}) утверждение ¬(x ⋁ y ⋁ z) = ¬x ⋀ ¬y ⋀ ¬z', end=' ')
            if not(x or y or z) == (not x) and (not y) and (not z):
                print('Истинно')
            else:
                print('Ложно')
