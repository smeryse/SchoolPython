print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = ((x <= y) and (y <= w) or (z == (x or y)))
                if f == 0:
                    print(x, y, z, w)