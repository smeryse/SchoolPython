# nums = list(range(1016, 7937+1))

# task_1
# finilly = []
# for num in nums:
#     if num % 3 == 0 and num % 7 > 0 and num % 17 > 0 and num % 19 > 0 and num % 27 > 0:
#         finilly.append(num)
#
# print(len(finilly),
#       max(finilly),
#       sep='\n'
#       )

# task_2
# f = open('../file/17-345.txt')
# lst = [int(i) for i in f]
#
# print(sum(lst))
# f = open('../file/17-345.txt')
# lst = [int(i) for i in f]
#
# filish = [int(i) for i in lst if int(i) % 3 == 0]
#
# print(sum(filish))

# task_3
# f = open('../file/17-4.txt')
# lst = [int(i) for i in f]
#
# nums = []
# for i in lst:
#     if i % 3 == 0 and i % 7 > 0 and i % 17 > 0 and i % 19 > 0 and i % 27 > 0:
#         nums.append(i)
#
# print(len(nums),
#       max(nums),
#       sep='\n'
#       )

# task_4
# f = open('../file/17-345.txt')
# lst = [int(i) for i in f]
#
# count = 0
# for i in range(0, len(lst) - 1):
#     if lst[i] % 10 == 0 or lst[i+1] % 10 == 0:
#         count += 1
#
# print(count)

# task_5
# f = open('../file/17-257.txt')
# lst = [int(i) for i in f]
#
# a, b = [], []
#
# for i in lst:
#     if i % 11 == 0:
#         a.append(i)
#     if i % 17 == 0:
#         b.append(i)
#
# if len(a) > len(b):
#     print(len(a),
#           min(a),
#           sep='\n'
#           )
# else:
#     print(len(b),
#           min(b),
#           sep='\n'
#           )

# task_6
# f = open('../file/17-257.txt')
# lst = [int(i) for i in f]
#
# k2 = [i for i in lst if i % 2 == 0]
# nk2 = [i for i in lst if i % 2 != 0]
#
# if max(k2) > max(nk2):
#     print(
#         len(k2),
#         min(nk2),
#         sep='\n'
#     )

# task_7
# nums = open('../../../../8 задание/file/17-4.txt')
# nums = [int(i) for i in nums]
#
# correct = []
# for i in nums:
#     if i % 13 == 4 and i % 8 == 1:
#         correct.append(i)
#
# print(max(correct),
#       sum(correct)
#       )

