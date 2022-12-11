from itertools import product

count = 0


for i in product('ABCX', repeat=5):
    if (i[0] == 'X' or i[-1] == 'X') and i.count('X') == 1:
        print(i)
        count += 1

# from itertools import product
#
#
# count = 0
# for i in product('АВСХ', repeat=5):
#     if i.count('Х') == 1:
#         print(*i, sep='')
#         count += 1
#
# print(count)

# count = 0
# itr = ['', '', '', '']
# for itr[0] in 'ABCDXYZ':
#     for itr[1] in 'ABCDXYZ':
#         for itr[2] in 'ABCDXYZ':
#             for itr[3] in 'ABCDXYZ':
#                 if (itr[0] in 'XYZ') and ([True for j in itr[1:] if j in 'ABCD'] == [True, True, True]):
#                     count += 1
#                     print(itr)
#
# print(count)

# count = 0
# for i in product('ОГЭИНФ', repeat=6):
#     i = ''.join(i)
#     if (i[0] == 'Э' or i[0] == 'О') and i[4:6] == 'НФ' and i.count('ИГ') >= 1 and 'ОГЭ' not in i:
#         print(i)
#         count += 1
#
# print(count)

# for i in product("СОТКАПЛЗ", repeat=5):
#     i = ''.join(i)
#     if i[-1] != 'О' and i[-1] != 'А' and i.count('ЗЛО') == 0 and [True for j in i if i.count(j) == 1] == [True, True, True, True, True]:
#         count += 1
#
# print(count)

# for i in product('ВАЙФУ', repeat=4):
#     i = ''.join(i)
#     if i[0] != 'Й' and i.count('ВФ') == 0 and i.count('ФВ') == 0 and i.count(i[0]) == 1 and i.count(i[1]) == 1 \
#         and i.count(i[2]) == 1 and i.count(i[3]) == 1:
#         count += 1
#         print(i)

# Homework tasks
# 1
# for i in product('ABCX', repeat=4):
#     if i.count('X') == 1 and (i[0] == 'X' or i[-1] == 'X'):
#         count += 1
#         print(*i)

# 2
# for i in product('ABX', repeat=6):
#     if i.count('X') == 1:
#         count += 1
#         print(i)

# 3
# for i in product('ABCDEF', repeat=5):
#     if i[0] != "F" and i[-1] != 'A':
#         count += 1
#         print(i)

# 4
# for i in product('ABCDEX', repeat=4):
#     if i.count('X') == 1 and (i[0] == 'X' or i[-1] == 'X'):
#         count += 1
#         print(i)

# 5
# for i in product('АБВГ', repeat=6):
#     i = ''.join(i)
#     if i[0] != 'А' and i.count('АА') == 0 and i.count('ББ') == 0 and i.count('ВВ') == 0 and i.count('ГГ') == 0:
#         count += 1
#         print(i)


# for i in product('ЛЕВИЙ', repeat=5):
#     i = ''.join(i)
#     if i[0] != 'Й' and i.count('ЕИ') == 0 and i.count('Л') == 1 \
#             and i.count('Е') == 1 and i.count('В') == 1 \
#             and i.count('И') == 1 and i.count('Й') == 1:
#         count += 1
#         print(i)

# for i in product('МАТВЕЙ', repeat=6):
#     i = ''.join(i)
#     if i[0] != 'Й' and i.count('М') == 1 and i.count('А') == 1 and i.count('Т') == 1 and \
#             i.count('В') == 1 and i.count('Е') == 1 and i.count('Й') == 1 and 'АЕ' not in i:
#         count += 1
#         print(i)

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

# for i in product(['0', '1', '2', '3', '4'], repeat=6):
#     i = ''.join(i)
#     if int(i, 5) % 2 == 0 and i[0] == '3':
#         count +=1
#         print(i)
print(count)
