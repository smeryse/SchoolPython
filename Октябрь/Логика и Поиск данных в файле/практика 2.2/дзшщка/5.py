#
print('x, y, w, z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
                if f == 1:
                    for i in [x, y, w, z]:
                        print(str(i).ljust(3), end='')
                    print()
