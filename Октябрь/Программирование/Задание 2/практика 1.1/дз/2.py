from files import *

nums = process('https://kpolyakov.spb.ru/cms/files/ege-seq/17-4.txt')

res= []
for i in nums:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        res.append(i)

print(
    max(res) - min(res),
    len(res)
)