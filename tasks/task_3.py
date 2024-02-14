line: list[str, ...] = input().split()

if not line:
    print('никто не оценил это')
else:
    if (ppl_count := len(line)) >= 4:
        first, second, *others = line
        likes_text = f'{first}, {second} и еще {len(others)} человека'
    elif ppl_count == 3:
        first, second, third = line
        likes_text = f'{first}, {second} и {third}'
    else:
        likes_text = ' и '.join(line)

    print(f'{likes_text} понравилось это')
