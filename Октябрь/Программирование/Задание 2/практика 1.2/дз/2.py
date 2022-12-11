f = open('17-1.txt')
file = [int(i) for i in f]

middle = sum(file) / len(file)

res = []
for i in range(0, len(file) - 1):
    if (file[i] > middle and file[i] % 17 == 0) or (file[i] > middle and file[i+1] % 17 == 0)\
        or (file[i+1] > middle and file[i] % 17 == 0) or (file[i+1] > middle and file[i+1] % 17 == 0):
        res.append(sum(file[i:i+2]))

print(
    len(res),
    max(res)
)