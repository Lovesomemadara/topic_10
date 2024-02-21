# names: list[str, ...] = [name for name in input().split(',')]
#
# commands: list[list[str, ...]] = [
#     part.split(' ')
#     for part in (input().split(','))
# ]

names: list[str, ...] = input().split(',')
commands: list[str, ...] = input().split(',')

for command in commands:
    parts: list[str, ...] = command.split(' ')
    artist: str = parts[0]
    change: int = int(parts[1])

    index = names.index(artist)
    names.remove(artist)
    names.insert(index - change, artist)

print(names)
