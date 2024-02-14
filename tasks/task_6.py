line: list[int, ...] = list(map(int, input().split()))
num: int = int(input())

# del_counter: int = 0
if not line:
    print('Пустой список')
elif num not in line:
    print('Элемент не найден')
else:
    # while num in line:
    #     line.remove(num)
    #     del_counter += 1
    # TODO: Можно решить в одну строку, через генератор списков
    result: list[int, ...] = []
    for curr_num in line:
        if curr_num != num:
            result.append(curr_num)

    # print(f'Удалено {del_counter} элементов')
    print(f'Удалено {len(line) - len(result)} элементов')
    print(f'Новый список: {line}')
