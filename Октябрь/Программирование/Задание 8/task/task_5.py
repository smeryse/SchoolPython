f = open('../file/17-345.txt')
lst = [int(i) for i in f]

count = 0
for i in range(0, len(lst) - 1):
    if lst[i] % 10 == 0 or lst[i+1] % 10 == 0:
        count += 1

print(count)