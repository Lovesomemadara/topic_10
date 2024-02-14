line: list[int, ...] = list(map(int, input().split()))
num: int = int(input())

del_counter: int = 0
if not line:
    print('Пустой список')
else:
    if num in line:
        while num in line:
            line.remove(num)
            del_counter += 1
        print(f'Удалено {del_counter} элементов')
        print(f'Новый список: {line}')
    else:
        print('Элемент не найден')
