# TODO: Здесь лучше примегить генератор списков
nums: list[int, ...] = list(map(int, input().split()))

length: int = len(nums)
result: list[int, ...] = []
for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            break
    else:
        result.append(str(nums[i]))

print(' '.join(result) or False)
