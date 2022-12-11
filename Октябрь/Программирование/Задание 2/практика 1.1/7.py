print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = not(w <= z) or (x <= y) or not(x)
                if f == 0:
                    print(x, y, z, w)