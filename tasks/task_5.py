line: list[str, ...] = input().split()
num: int = int(input())

more_counter: int = 0
for curr_num in line:
    if num < int(curr_num):
        more_counter += 1
if more_counter == 0:
    print(-1)
else:
    print(more_counter)
