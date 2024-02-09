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
