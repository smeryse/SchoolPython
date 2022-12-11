f = open('17-205.txt')
file = [int(i) for i in f]

res = []
for i in range(0, len(file) - 1):
    if (file[i] % 7 == 0 or file[i+1] % 7 == 0) and sum(file[i:i+2]) % 5 == 0:
        res.append(sum(file[i:i+2]))

print(
    len(res),
    max(res)
)