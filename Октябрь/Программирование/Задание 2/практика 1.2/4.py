f = open('17-345.txt')
file = [int(i) for i in f]

res = []
for i in range(0, len(file) - 1):
    if (file[i] < max(file) - min(file) and file[i+1] > max(file) - min(file))\
            or (file[i+1] < max(file) - min(file) and file[i] > max(file) - min(file)):
        res.append(sum(file[i:i+2]))

print(
    len(res),
    max(res)
)

#40 19222 its correct