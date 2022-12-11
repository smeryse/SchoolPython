nums = open('../file/17-4.txt')
nums = [int(i) for i in nums]

correct = []
for i in nums:
    if i % 13 == 4 and i % 8 == 1:
        correct.append(i)

print(max(correct),
      sum(correct)
      )
