f = open('17-257.txt')
file = [int(i) for i in f]

c2 = [i for i in file if i % 2 == 0]
nc2 = [i for i in file if i % 2 != 0]

if max(c2) > max(nc2):
    print(
        len(c2),
        min(c2)
    )
else:
    print(
        len(nc2),
        min(nc2)
    )

#507 268 its correct