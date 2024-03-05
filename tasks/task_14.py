nums = [int(x) for x in input().split()]
merged_tiles = [n for n in nums if n != 0]

i = 0
while i < len(merged_tiles) - 1:
    if merged_tiles[i] == merged_tiles[i + 1] != 0:
        merged_tiles[i] *= 2
        merged_tiles.pop(i + 1)

        if len(nums) != len(merged_tiles):
            merged_tiles.extend([0] * (len(nums) - len(merged_tiles)))

    i += 1

print(merged_tiles)
