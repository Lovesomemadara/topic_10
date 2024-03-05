names: list[str, ...] = input().split(',')

for command in input().split(','):
    artist, change = command.split(' ')
    index: int = names.index(artist)
    names.insert(index - int(change), names.pop(index))

print(names)
