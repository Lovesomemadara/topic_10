line: list[str, ...] = input().split(', ')
k: int = int(input())

line.sort(key=len, reverse=True)

print(line[:k])
