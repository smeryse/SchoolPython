with open('26 (1).txt', 'r') as f:
    theatre = {}
    for string in f.readlines():
        row, seat_num = [int(i) for i in string.split()]
        theatre.setdefault(row, []).append(seat_num)


for row, seat_num in sorted(theatre.items(), reverse=True):
    if seat_num >= 3:
        pass
    print(f'{row}: {sorted(seat_num, reverse=True)}')

# описать проверку на соседние места