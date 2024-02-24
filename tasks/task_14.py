nums: list[int, ...] = [int(x) for x in input().split()]

merged_tiles: list[int, ...] = [0] * len(nums)
i: int = 0
for tile in nums:
    if tile != 0:
        if merged_tiles[i] == 0:
            merged_tiles[i] = tile
        elif merged_tiles[i] == tile:
            merged_tiles[i] *= 2
            i += 1
        else:
            i += 1
            merged_tiles[i] = tile

print(merged_tiles)
