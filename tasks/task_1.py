values: list[str, ...] = []

while True:
    value: str = input()
    stop_flag = value.lower() == 'конец'
    if values and stop_flag:
        break
    elif not values and stop_flag:
        print('Ничего не введено')
        break
    else:
        values.append(value)

if values:
    result: str = ','.join(values)
    print(result)

# Option 2
# -------------------------------
values: list[str, ...] = []

while True:
    value: str = input()
    if value.lower() == 'конец':
        break
    values.append(value)

if values:
    result: str = ','.join(values)
    print(result)
else:
    print('Ничего не введено')

# Option 3
# -------------------------------
values: list[str, ...] = []
while (value := input()).lower() != 'конец':
    values.append(value)

if values:
    print(','.join(values))
else:
    print('Ничего не введено')
