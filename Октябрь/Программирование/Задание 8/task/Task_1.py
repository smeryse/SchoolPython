nums = list(range(1016, 7937+1))

finilly = []
for num in nums:
    if num % 3 == 0 and num % 7 > 0 and num % 17 > 0 and num % 19 > 0 and num % 27 > 0:
        finilly.append(num)

print(len(finilly),
      max(finilly),
      sep='\n'
      )
