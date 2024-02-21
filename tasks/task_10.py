nums: list[int, ...] = [int(x) for x in input().split()]

length: int = len(nums)
result: list[str, ...] = []
for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            break
    else:
        result.append(str(nums[i]))

print(' '.join(result) or False)
