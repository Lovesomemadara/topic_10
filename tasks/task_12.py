nums: list[int, ...] = [int(x) for x in input().split()]

result: list[int, ...] = []

i: int = 0
while i < len(nums):
    if (i + 1) == len(nums):
        result.append(nums[i - 1] + nums[0])
        break
    result.append(nums[i + 1] + nums[i - 1])
    i += 1

print(result)
