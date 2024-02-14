line: list[str, ...] = input().split(', ')
k: int = int(input())

sort_cities: list[str, ...] = sorted(line, key=len, reverse=True)
result = sort_cities[:k]
print(result)
