f = open('17-4.txt')
file = [int(i) for i in f]

middle = sum(file) / len(file)
res = []
for i in range(0, len(file) - 1):
    if (file[i] > middle or file[i+1] > middle) and sum(file[i:i+2]) % 10 == 9:
        res.append(sum(file[i:i+2]))

print(len(res), min(res))