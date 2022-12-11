f = open('17-4.txt')
file = [int(i) for i in f]

res = []
for i in file:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        res.append(i)

print(max(res) - min(res), len(res))