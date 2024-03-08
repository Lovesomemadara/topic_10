nums: list[int] = [int(x) for x in input().split('x')]

array: list[str] = ['*' * nums[-1]]
for size in nums[::-1][1:]:
    array: list[list[str]] = [array] * size

for sublist in array:
    for line in sublist:
        print(' '.join(line))
    print()
