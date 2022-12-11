f = open("17-257.txt")
file = [int(i) for i in f]

c7 = [i for i in file if i % 7 == 0]
c13 = [i for i in file if i % 13 == 0]

if min(c7) > min(c13):
    print(len(c7), max(c7))
else:
    print(len(c13), max(c13))