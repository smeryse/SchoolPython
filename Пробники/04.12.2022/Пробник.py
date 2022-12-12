# n = int(input())
# r = bin(n)[2:]
#
# if n % 2 == 0:
#     r = '11' + r + '11'
# else:
#     r = '1' + r + '0'
#
# print(int(r, 2))

# from itertools import product
#
# alphas = ['А', 'Б', 'Г', 'О', 'Щ']
# alphas.sort(reverse=True)
#
# count = 1
# for word in product(alphas, repeat=6):
#     word = ''.join(word)
#     print(f'count: {count}, word: {word}')
#     if word == 'ОБЩАГА':
#         break
#     count += 1

# nums = '8' * 125
# while ('888' in nums) or ('333' in nums):
#     if '333' in nums:
#         nums = nums.replace('333', '8', 1)
#     else:
#         nums = nums.replace('888', '3', 1)
#
# print(nums
#task_14
# f = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15 ** 11 + 18338
# new_sys = []
# while f > 1:
#     new_sys.append(f % 15)
#     f = f // 15
#
# new_sys.reverse()
# result = set(new_sys)
#
# print(result, len(result))

#task_15
# def dels(n, m):
#     if n % m == 0:
#         return 1
#     else:
#         return 0
#
# result = []
# a = 1
# while len(result) != 4:
#     flag = True
#     for x in range(0, 1000):
#         f = (not (dels(x, 16) == dels(x, 24))) <= dels(x, a)
#         if f == 1:
#             continue
#         else:
#             flag = False
#             break
#     if flag:
#         result.append(a)
#     else:
#         continue
#     a += 1
#
# print(result)

#task_17
# with open('C:/Users/Ярослав/Downloads/17-257.txt', 'r') as f:
#     nums = f.read().split()
#     f.close()
#
# odd = [10000, 0]
# nums = [int(i) for i in nums]
# for i in nums:
#     if i % 2 == 1 and i > odd[1]:
#         max_odd = i
#     elif i % 2 == 1 and i < odd[0]:
#         min_odd = i
#
# even_sum = []
# for i in range(1, len(nums)):
#     if (nums[i] + nums[i - 1]) % 2 == 0:
#         even_sum.append([nums[i], nums[i - 1]])
#
# result_sum, count = [], 0
# for res in even_sum:
#     if sum(res) > sum(odd):
#         result_sum.append(sum(res))
#         count += 1
#
# print(min(result_sum), count, sep='\n')

#task_24
# with open('C:/Users/Ярослав/Downloads/24-157.txt', 'r') as f:
#     alphas = f.read()
#     f.close()
#
# lens = []
# alphas = alphas.split('QW')
# print(type(alphas))
# for l in alphas:
#     lens.append(len(l))
#
# print(max(lens))

#task_25
# #input: [174457, 174505]
#
# result = []
# for num in range(174457, 174506):
#     devider = []
#     for dev in range(2, num):
#         if num % dev == 0:
#             devider.append(dev)
#     if len(devider) == 2:
#         result.append(devider)
#
# #nums output
# for i in result:
#     print(*i)
