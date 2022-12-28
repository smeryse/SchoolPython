# task_1
# def f(n, finish):
#     if n == finish:
#         return 1
#     elif n > finish or n == 8:
#         return 0
#     return f(n + 1, finish) + f(n + 2, finish)
#
# print(f(3, 13))
# answer = 25

# task_2
# def f(start, finish):
#     if start == finish:
#         return 1
#     elif start > finish or start == 10 or start == 15:
#         return 0
#     return f(start + 1, finish) + f(start + 2, finish) + f(start + 3, finish)
#
# print(f(5, 11) * f(11, 18))
# answer = 176

# task_3
# def f1(n, f):
#     if n == f:
#         return 1
#     elif n < f:
#         return 0
#     return f1(n - 8, f) + f1(n // 2, f)
#
# print(f1(102, 43) * f1(43, 5))
# answer = 8

# task_4
# def f1(n, f):
#     if n == f:
#         return 1
#     elif n > f or n == 12:
#         return 0
#     return f1(n + 1, f) + f1(n + 3, f) + f1(n * 2, f)
#
# print(f1(3, 8) * f1(8, 21))
# answer = 228

# task_5
# def f(st, fin):
#     if st == fin:
#         return 1
#     elif st > fin:
#         return 0
#     return f(st * 2, fin) + f(st * 3, fin)
#
# print(f(8, 96) * f(96, 3456))
# answer = 18

# task_6
from itertools import product
#
# result = []
#
#
# def f(n, step):
#     if step == 5:
#         result.append(n)
#     else:
#         f(n + 2, step + 1)
#         f(n + 3, step + 1)
#         f(n * 2, step + 1)
#
# f(10, 0)
# print(len(set(result)))