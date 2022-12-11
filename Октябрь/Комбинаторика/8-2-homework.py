from itertools import product

# alphas = ['В', 'И', 'Н', 'Т']
# alphas.sort()
#
# count = 1
# for i in product(alphas, repeat=5):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#     count += 1
#
# answer = 'ТТТНТ'


# count = 1
# for i in product('БКФ', repeat=6):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#     count += 1
# count = 1
# for i in product('ЕЖИ', repeat=6):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#     count += 1
# count = 1
# alpha = list('МУХА')
# alpha.sort()

# for i in product(alpha, repeat=4):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#
#     if i == 'ХУХХ':
#         result = count
#     count += 1
#
# print(result)
#answer = 240

#task_5
# count = 1
# alpha = list('ВЕКНО')
# alpha.sort()
# result = []
#
# for i in product(alpha, repeat=5):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#
#     if i[0] == 'О':
#         result.append((count, i))
#     count += 1
#
# print(result)
#answer = 2501

#task_6
count = 1
alpha = list('СВЕТ')
alpha.sor()
result = []

for i in product(alpha, repeat=5):
    i = ''.join(i)
    print(f'{count}: {i}')

    if i[0] == 'Т':
        result.append((count, i))
    count += 1

print(result)