names: list[str, ...] = input().split(',')

for command in input().split(','):
    artist, change = command.split(' ')

    # parts: list[str, ...] = command.split(' ')
    # artist: str = parts[0]
    # change: int = int(parts[1])

    index: int = names.index(artist)

    # names.remove(artist)
    # names.insert(index - int(change), artist)

    names.insert(index - int(change), names.pop(index))

print(names)
