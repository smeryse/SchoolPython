f = open('17-1.txt')
file = [int(i) for i in f]

res = []
mini = []
for i in range(1, len(file) - 1):
    if file[i-1] < file[i] > file[i+1]:
        res.append(file[i])
        mini.append(i)

res.sort()

print(len(res),
      min(mini)
      )

#its correct 3316 2