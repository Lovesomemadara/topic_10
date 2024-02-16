# n: int = int(input())
# print(len([num for num in list(map(int, input().split())) if num > n]) or -1)

# -------------------------------------------------------

line: list[int, ...] = list(map(int, input().split()))
n: int = int(input())
print(len([num for num in line if num > n]) or -1)
