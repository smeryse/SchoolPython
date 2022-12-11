f = open('../file/17-345.txt')
lst = [int(i) for i in f]

filish = [int(i) for i in lst if int(i) % 3 == 0]

print(sum(filish))