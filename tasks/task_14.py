nums: list[int] = [int(x) for x in input().split()]
merged_tiles: list[int] = [n for n in nums if n != 0]

i: int = 0
while i < len(merged_tiles) - 1:
    if merged_tiles[i] == merged_tiles[i + 1] != 0:
        merged_tiles[i] *= 2
        merged_tiles.pop(i + 1)
    i += 1

merged_tiles.extend([0] * (len(nums) - len(merged_tiles)))
print(merged_tiles)
