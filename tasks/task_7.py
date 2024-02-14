line: list[str, ...] = input().split()
print(min(line, key=len))
print(max(line, key=len))
