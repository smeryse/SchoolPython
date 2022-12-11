f = open('17-10.txt')
file = [int(i) for i in f]

res = []
for i in range(0, len(file) - 1):
    num = str(sum(file[i:i+2]))
    if len(num) == 3 and int(num[-1]) > int(num[-2]):
        res.append(num)

print(
    len(res),
    min(res)
)