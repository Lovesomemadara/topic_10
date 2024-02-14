line: list[str, ...] = input().split()

correct_lst: list[str, ...] = []
print(f'ID списка: {id(line)}')
for item in line:
    if item not in correct_lst:
        correct_lst.append(item)
    else:
        del line[int(item)]

print(f'Исходный список: {line}')
print(f'ID списка: {id(correct_lst)}')
print(f'Измененный список: {correct_lst}')

if len(line) == len(correct_lst):
    print('В списке не найдено дубликатов')
else:
    print(f'Удалено {len(line) - len(correct_lst)} дубликатов')

# Подсказка к задаче:
text = 'abccc'
for i in range(len(text)):
    text = text.replace('c', '')
    print(text[i])

text = 'abccc'
i = 0
while i < len(text):
    text = text.replace('c', '')
    print(text[i])
    i += 1
