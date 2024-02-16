nums: list[int, ...] = list(map(int, input().split()))

result: list[int, ...] = [nums[num] for num in range(1, len(nums))
                          if nums[num] > nums[num - 1]]

print(' '.join(map(str, result)) or False)