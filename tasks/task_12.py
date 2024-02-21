nums: list[int, ...] = [int(x) for x in input().split()]


# ------------------- Option 1
result: list[int, ...] = []
length: int = len(nums)
i: int = 0
while i < length:
    if (i + 1) == length:
        result.append(nums[i - 1] + nums[0])
        break
    result.append(nums[i + 1] + nums[i - 1])
    i += 1

print(result)

# ------------------- Option 2
result: list[int, ...] = []
length: int = len(nums)
for i in range(length):
    left_neighbor: int = nums[i - 1]
    right_neighbor: int = nums[(i + 1) % length]
    total_neighbors: int = left_neighbor + right_neighbor
    result.append(total_neighbors)

print(result)

# ------------------- Option 3
print([nums[i - 1] + nums[(i + 1) % length] for i in range(length)])
