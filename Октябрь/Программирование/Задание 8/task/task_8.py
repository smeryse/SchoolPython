f = open('../file/17-1.txt')
lst = [int(i) for i in f]

summ = []
for i in range(0, len(lst) - 1):
    if (lst[i] % 7 == 0 and lst[i+1] % 17 != 0) or (lst[i+1] % 7 == 0 and lst[i] % 17 != 0):
        summ.append(lst[i] + lst[i+1])

print(len(summ),
      min(summ),
      )