nums: list[int, ...] = list(map(int, input().split()))

correct_nums: dict[int, ...] = {}
for num in nums:
    if num in correct_nums:
        correct_nums[num] += 1
    else:
        correct_nums[num] = 1

result: list[str, ...] = []
for num in nums:
    if correct_nums[num] == 1:
        result.append(str(num))

if len(result) > 0:
    print(' '.join(result))
else:
    print(False)
