line: list[int, ...] = list(map(int, input().split()))
num: int = int(input())

if not line:
    print('Пустой список')
elif num not in line:
    print('Элемент не найден')
else:
    result: list[int, ...] = [curr_num for curr_num in line if curr_num != num]

    print(f'Удалено {len(line) - len(result)} элементов')
    print(f'Новый список: {result}')
