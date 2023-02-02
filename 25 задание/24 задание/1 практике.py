#task_1
# f = open('Файлы/1, 2.txt').read()
#
# c = 1
# lst = []
# for i in range(0, len(f) - 1):
#     if f[i] != f[i + 1]:
#         c += 1
#     else:
#         lst.append(c)
#         c = 1
# print(max(lst))

#task_2
# 1 решение
# f = open('Файлы/1, 2.txt').read()
#
# c = 1
# result = []
# for i in range(len(f) - 1):
#     if f[i] == f[i + 1] == 'X':
#         c += 1
#     else:
#         result.append(c)
#         c = 1
#
# print(max(result))

# 2 решение
# f = f.replace('Y', ' ').replace('Z', ' ').split()
# print(max([len(i) for i in f]))

# 3 task
# f = open('Файлы/24-196.txt').read()
# f = f.replace('ZY', '1').replace('ZX', '1')
#
# for i in range(1, 10000):
#     if '1' * i in f:
#         print(i)

# task 4
# files = open('Файлы/inf_22_10_20_24.txt').readlines()
# lines = [file[:-1] for file in files]
# count = 0
# for line in lines:
#     if line.count('E') > line.count('A'):
#         count += 1
#
# print(count)

# task_5
# line = open('Файлы/24.txt').read()
# alphas = dict()
# for i in range(len(line) - 1):
#     if line[i] == 'A':
#         alphas[line[i + 1]] = alphas.get(line[i + 1], 0) + 1
#
# print(max(alphas.items(), key=lambda x: x[1]))