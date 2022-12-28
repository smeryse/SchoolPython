# task_1
# def f(n, finish):
#     if n == finish:
#         return 1
#     elif n > finish or n == 14:
#         return 0
#     return f(n + 1, finish) + f(n * 2, finish) + f(n * 3, finish)
#
# print(f(1, 12) * f(12, 40))
# answer = 152

# task_2
# def f(n, finish):
#     if n == finish:
#         return 1
#     elif n > finish:
#         return 0
#     return f(n + 1, finish) + f(n * 2, finish)
#
# print(f(2, 11) * f(11, 25) * f(25, 50))
# answer = 42

# task_3
# def f(n, finish):
#     if n == finish:
#         return 1
#     elif n > finish or n == 30:
#         return 0
#     return f(n + 1, finish) + f(n * 2, finish) + f(n * 3, finish)
#
# print(f(2, 13) * f(13, 39))
# answer = 75

# task_4
# def f(n, finish):
#     if n == finish:
#         return 1
#     elif n < finish:
#         return 0
#     return f(n - 8, finish) + f(n // 2, finish)
#
# print(f(102, 43) * f(43, 5))
# answer = 8

# task_5
# def f(n, finish):
#     if n == finish:
#         return 1
#     elif n > finish:
#         return 0
#     return f(n + 1, finish) + f(n * 2, finish) + f((n + 1, n + 2)[n % 2], finish)
#
# print(f(3, 9) * f(9, 17) * f(17, 25))
# answer = 229635
