f = open('17-336.txt')
file = [int(i) for i in f]

M = int(max([int(i) for i in file if i % 37 == 0]))
print(M)
res = []
for i in range(0, len(file) - 1):
    if file[i] % M == 0 or file[i+1] % M == 0:
        res.append(sum(file[i:i+2]))

print(
    len(res),
    min(res)
)

#2 124339 its correct (2)