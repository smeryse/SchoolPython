print('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = ((x or y) <= (z == x))
            if f == 0:
                print(x, y, z)