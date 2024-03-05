nums: list[int, ...] = [int(x) for x in input().split('x')]

array: list[str, ...] = ['*' * nums[-1]]
for size in nums[::-1][1:]:
    inner_array: list[list[str, ...]] = [array] * size
    array: list[str, ...] = inner_array

for sublist in array:
    for line in sublist:
        print(' '.join(line))
    if len(nums) == 3:
        print()
