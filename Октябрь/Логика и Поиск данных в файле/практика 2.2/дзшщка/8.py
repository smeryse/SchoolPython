#
print('x, y, w, z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x and (not(y))) or (y == z) or w
                if f == 0:
                    for i in [x, y, w, z]:
                        print(str(i).ljust(3), end='')
                    print()
