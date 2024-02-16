line: list[str, ...] = input().split()

print(f'ID списка: {id(line)}')
print(f'Исходный список: {line}')

i: int = 0
delete_counter: int = 0
while i < len(line):
    j: int = i + 1
    while j < len(line):
        if line[i] == line[j]:
            del line[j]
            delete_counter += 1
        else:
            j += 1
    i += 1

print(f'ID списка: {id(line)}')
print(f'Измененный список: {line}')

print('В списке не найдено дубликатов' if not delete_counter
      else f'Удалено {delete_counter} дубликатов')
