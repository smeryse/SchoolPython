# import time
# from itertools import product

# task_1
# def main():
#     alpha = ['Г', 'О', 'Д']
#
#     count = 0
#     for one in alpha:
#         for two in alpha:
#             for three in alpha:
#                 for four in alpha:
#                     for five in alpha:
#                         for six in alpha:
#                             if one != 'О' and six != 'О':
#                                 count += 1
#     print(count)
#
#
# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))

# task_2
# def main():
#     string = 'МЕТРО'
#     count = 0
#     for i in product(string, repeat=4):
#         if i[0] != 'Р' and i[0] != 'Т' and i[0] != 'М' and i[-1] != 'Е' and i[-1] != 'О':
#             print(*i, sep='')
#             count += 1
#     print(count)
#
# start_time = time.time()
# main()
# print(f"--- {time.time() - start_time} seconds ---")

# task_3
# def main():
#     string = 'МЕТРО'
#     count = 0
#     for one in string:
#         for two in string:
#             for three in string:
#                 for four in string:
#                     if one != 'Р' and one != 'Т' and one != 'М' and four != 'Е' and four != 'О':
#                         print(one, two, three, four, sep='')
#                         count += 1
#     print(count)
#
# start_time = time.time()
# main()
# print(f"--- {time.time() - start_time} seconds ---")

# task_4
# count = 0
# for i in product('ABCX', repeat=5):
#     if (i[0] == 'X' or i[-1] == 'X') and i.count('X') == 1:
#         print(i)
#         count += 1


# task_5
# count = 0
# for i in product('АВСХ', repeat=5):
#     if i.count('Х') == 1:
#         print(*i, sep='')
#         count += 1
#
# print(count)

# task_6
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

# task_7
# count = 0
# for i in product('ОГЭИНФ', repeat=6):
#     i = ''.join(i)
#     if (i[0] == 'Э' or i[0] == 'О') and i[4:6] == 'НФ' and i.count('ИГ') >= 1 and 'ОГЭ' not in i:
#         print(i)
#         count += 1
#
# print(count)

# task_8
# for i in product("СОТКАПЛЗ", repeat=5):
#     i = ''.join(i)
#     if i[-1] != 'О' and i[-1] != 'А' and i.count('ЗЛО') == 0 \
#     and [True for j in i if i.count(j) == 1] == [True, True, True, True, True]:
#         count += 1
#
# print(count)

# task_9
# for i in product('ВАЙФУ', repeat=4):
#     i = ''.join(i)
#     if i[0] != 'Й' and i.count('ВФ') == 0 and i.count('ФВ') == 0 and i.count(i[0]) == 1 and i.count(i[1]) == 1 \
#         and i.count(i[2]) == 1 and i.count(i[3]) == 1:
#         count += 1
#         print(i)
