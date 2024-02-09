line: list[str, ...] = input().split()

# if not line:
#     print('Пустой список')
# else:
#     for index, item in enumerate(line):
#         print(f'{int(item)} {index}')

length: int = len(line)

if length == 0:
    print('Пустой список')
else:
    i: int = 0
    while i < length:
        print(f'{line[i]} {i}')
        i += 1
