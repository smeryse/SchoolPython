# Homework tasks
# task_1
# for i in product('ABCX', repeat=4):
#     if i.count('X') == 1 and (i[0] == 'X' or i[-1] == 'X'):
#         count += 1
#         print(*i)

# task_2
# for i in product('ABX', repeat=6):
#     if i.count('X') == 1:
#         count += 1
#         print(i)

# task_3
# for i in product('ABCDEF', repeat=5):
#     if i[0] != "F" and i[-1] != 'A':
#         count += 1
#         print(i)

# task_4
# for i in product('ABCDEX', repeat=4):
#     if i.count('X') == 1 and (i[0] == 'X' or i[-1] == 'X'):
#         count += 1
#         print(i)

# task_5
# for i in product('АБВГ', repeat=6):
#     i = ''.join(i)
#     if i[0] != 'А' and i.count('АА') == 0 and i.count('ББ') == 0 and i.count('ВВ') == 0 and i.count('ГГ') == 0:
#         count += 1
#         print(i)

# task_6
# for i in product('ЛЕВИЙ', repeat=5):
#     i = ''.join(i)
#     if i[0] != 'Й' and i.count('ЕИ') == 0 and i.count('Л') == 1 \
#             and i.count('Е') == 1 and i.count('В') == 1 \
#             and i.count('И') == 1 and i.count('Й') == 1:
#         count += 1
#         print(i)

# task_7
# for i in product('МАТВЕЙ', repeat=6):
#     i = ''.join(i)
#     if i[0] != 'Й' and i.count('М') == 1 and i.count('А') == 1 and i.count('Т') == 1 and \
#             i.count('В') == 1 and i.count('Е') == 1 and i.count('Й') == 1 and 'АЕ' not in i:
#         count += 1
#         print(i)

# task_8
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

# task_9
# for i in product(['0', '1', '2', '3', '4'], repeat=6):
#     i = ''.join(i)
#     if int(i, 5) % 2 == 0 and i[0] == '3':
#         count +=1
#         print(i)
# print(count)

# task_10
# count = 1
# alpha = list('СВЕТ')
# alpha.sort()
# result = []
#
# for i in product(alpha, repeat=5):
#     i = ''.join(i)
#     print(f'{count}: {i}')
#
#     if i[0] == 'Т':
#         result.append((count, i))
#     count += 1
#
# print(result)
