f = open('17-4.txt')
file = [int(i) for i in f]

res = []
for i in file:
    if i % 13 == 4 and i % 8 == 1:
        res.append(i)

print(
    max(res),
    sum(res)
)