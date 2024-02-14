MESSAGE: str = 'понравилось это'

line: list[str, ...] = input().split()
ppl_count: int = len(line)

if not line:
    print('никто не оценил это')
else:
    if ppl_count >= 4:
        likes_text = f'{line[0]}, {line[1]} и еще {ppl_count - 2} человека'
    elif ppl_count == 3:
        likes_text = f'{", ".join(line[:2])} и {line[2]}'
    else:
        likes_text = ' и '.join(line)

    print(f'{likes_text} {MESSAGE}')
