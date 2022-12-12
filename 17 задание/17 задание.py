# task_1
# f = open('17-4.txt')
# file = [int(i) for i in f]
#
# res = []
# for i in file:
#     if i % 13 == 4 and i % 8 == 1:
#         res.append(i)
#
# print(
#     max(res),
#     sum(res)
# )

# task_2
# from files import *
#
# nums = process('https://kpolyakov.spb.ru/cms/files/ege-seq/17-4.txt')
#
# res= []
# for i in nums:
#     if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
#         res.append(i)
#
# print(
#     max(res) - min(res),
#     len(res)
# )

# task_3
# f = open('17-5.txt')
# file = [int(i) for i in f]
#
# res = []
# for i in range(0, len(file) - 1):
#     if file[i] % 2 == 0 or file[i+1] % 2 == 0:
#         res.append(file[i] + file[i+1])
#
# print(
#     len(res),
#     max(res)
# )

# task_4
# f = open('17-10.txt')
# file = [int(i) for i in f]
#
# res = []
# for i in range(0, len(file) - 1):
#     num = str(sum(file[i:i+2]))
#     if len(num) == 3 and int(num[-1]) > int(num[-2]):
#         res.append(num)
#
# print(
#     len(res),
#     min(res)
# )

# task_5
# f = open('17-205.txt')
# file = [int(i) for i in f]
#
# res = []
# for i in range(0, len(file) - 1):
#     if (file[i] % 7 == 0 or file[i+1] % 7 == 0) and sum(file[i:i+2]) % 5 == 0:
#         res.append(sum(file[i:i+2]))
#
# print(
#     len(res),
#     max(res)
# )
