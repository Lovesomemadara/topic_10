nums: list[int, ...] = []
reals: list[float, ...] = []
words: list[str, ...] = []

for item in input().split():
    if item.isnumeric() or item.startswith('+') or item.startswith('-'):
        nums.append(int(item))
    elif item.replace('.', '', 1).isdigit():
        reals.append(float(item))
    else:
        words.append(item)

print(nums or 'Список целых чисел пуст')
print(reals or 'Список вещественных чисел пуст')
print(words or 'Список остальных символов пуст')
