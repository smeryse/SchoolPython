f = open('../file/17-4.txt')
lst = [int(i) for i in f]

nums = []
for i in lst:
    if i % 3 == 0 and i % 7 > 0 and i % 17 > 0 and i % 19 > 0 and i % 27 > 0:
        nums.append(i)

print(len(nums),
      max(nums),
      sep='\n'
      )