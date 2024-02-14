# TODO: Здесь лучше примегить генератор списков
nums: list[int, ...] = list(map(int, input().split()))

result: list[str, ...] = []
for num in range(1, len(nums)):
    if nums[num] > nums[num - 1]:
        result.append(str(nums[num]))

print(' '.join(result) or False)
