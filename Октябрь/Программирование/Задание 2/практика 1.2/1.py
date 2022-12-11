f = open('17-257.txt')
file = [int(i) for i in f]

c11 = [i for i in file if i % 11 == 0]
c17 = [i for i in file if i % 17 == 0]

if len(c11) > len(c17):
    print(
        len(c11),
        min(c11)
    )
else:
    print(
        len(c17),
        max(c17)
    )

#it's correct
