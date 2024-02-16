nums: list[int, ...] = [int(x) for x in input().split()]

nums: list[str, ...] = [
    str(nums[i]) for i in range(1, len(nums))
    if nums[i] > nums[i - 1]
]

print(' '.join(nums) or False)
