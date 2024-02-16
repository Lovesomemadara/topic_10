line: list[int, ...] = [int(x) for x in input().split()]

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

# Option 2
i: int = 0
before_length: int = len(line)
was_seen: list = []
while i < len(line):
    if line[i] in was_seen:
        del line[i]
    else:
        was_seen.append(line[i])
        i += 1

after_length: int = len(line)

print(f'ID списка: {id(line)}')
print(f'Измененный список: {line}')

if before_length - after_length:
    print(f'Удалено {before_length - after_length} дубликатов')
else:
    print('В списке не найдено дубликатов')
