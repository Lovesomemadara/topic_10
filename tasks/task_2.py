NUMS_EMPTY: str = 'Список целых чисел пуст'
REALS_EMPTY: str = 'Список вещественных чисел пуст'
WORDS_EMPTY: str = 'Список остальных символов пуст'

nums: list[int, ...] = []
reals: list[float, ...] = []
words: list[str, ...] = []

line: list[str, ...] = input().split()

for item in line:
    plus: bool = item.startswith('+')
    minus: bool = item.startswith('-')
    if item.isnumeric() or plus or minus:
        nums.append(int(item[1:] if plus else item))
    elif item.replace('.', '', 1).isdigit():
        reals.append(float(item))
    else:
        words.append(item)

print(nums or NUMS_EMPTY)
print(reals or REALS_EMPTY)
print(words or WORDS_EMPTY)
