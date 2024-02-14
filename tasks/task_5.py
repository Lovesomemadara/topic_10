num: int = int(input())

more_counter: int = 0
for curr_num in input().split():
    if num < int(curr_num):
        more_counter += 1

print(more_counter or -1)

# TODO: Можно решить в одну строку, через генератор списков
