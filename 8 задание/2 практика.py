# from itertools import product
#
#

# task_1
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

# task_2
# count = 1
# for i in product('БКФ', repeat=6):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#     count += 1
# count = 1

# task_3
# for i in product('ЕЖИ', repeat=6):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#     count += 1
# count = 1
# alpha = list('МУХА')
# alpha.sort()

# task_4
# for i in product(alpha, repeat=4):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#
#     if i == 'ХУХХ':
#         result = count
#     count += 1
#
# print(result)
# answer = 240

# task_5
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
# answer = 2501

# task_6
# from itertools import product
#
# count = 0
# for i in product('ДЕЙКСТРА', repeat=6):
#     i = ''.join(i)
#     f = i.find('Й')
#     if f < len(i) - 1:
#         if i[f + 1] != 'Е' and i[f + 1] != 'Й' and i[f + 1] != 'А':
#             if i.count('Д') <= 1 and i.count('Е') <= 1 \
#                     and i.count('Й') <= 1 and i.count('К') <= 1 \
#                     and i.count('С') <= 1 and i.count('Т') <= 1 \
#                     and i.count('Р') <= 1 and i.count('А') <= 1:
#                 count += 1
#                 print(i)
#
# print(count)
