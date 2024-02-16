line: list[int, ...] = input().split()
n: int = int(input())

# Option 1
print(len([int(num) for num in line if int(num) > n]) or -1)

# Option 2
print(sum([1 for num in line if int(num) > n]) or -1)

# Option 3
counter = 0
for num in line:
    if int(num) > n:
        counter += 1
