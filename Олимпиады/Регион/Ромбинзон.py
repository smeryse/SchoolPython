# region input
n, m = map(lambda x: int(x), input().split())
crocs = dict()

move = {'W': (-1, 0),
        'N': (0, -1),
        'E': (1, 0),
        'S': (0, 1)}

for y in range(n):
    row = list(input())
    for x, value in enumerate(row):
        crocs[tuple(x, y)] = value    # делаем словарь: координата - направление

# endregion
# region main
run_out = []
for direction, cord in move.items():
    x, y = cord
    for croc in crocs:
        pass

# дописать нахождение оси движения, и сравнение, "есть ли кто-то на пути"

# endregion