# task_1
# def f(n):
#     if n < 3:
#         return 2 * n
#     elif n >= 3 and n % 2 == 0:
#         return 3 * n + 5 + f(n - 2)
#     elif n >= 3 and n % 2 == 1:
#         return n + 2 * f(n - 6)
#
# answer = f(61)
# print(answer)

# task_@
# def f(n):
#     if n < 1:
#         return n
#     elif n >= 1 and n % 2 == 0:
#         return n + 3 * f(n - 3)
#     elif n >= 1 and n % 2 == 1:
#         return 5 * n + 2 * f(n - 5)
#
# answer = f(30)
# print(answer)

# task_3
# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1 and n % 2 == 0:
#         return 2 * f(n - 1)
#     elif n > 1 and n % 2 == 1:
#         return 5 * n + f(n - 2)
#
# answer = f(64)
# print(answer)

# task_4
# def f(n):
#     if n <= 3:
#         return n
#     elif n > 3 and n % 2 == 0:
#         return 2 * n + f(n - 1)
#     elif n > 3 and n % 2 == 1:
#         return n ** 2 + f(n - 2)
#
#
# count = 0
# for n in range(1, 101):
#     if f(n) % 3 == 0:
#         count += 1
#
# print(count)

# task_5
# def f(n):
#     if n > 2:
#         return f(n - 1) + g(n - 2)
#     else:
#         return n
#
#
# def g(n):
#     if n > 2:
#         return g(n - 1) + f(n - 2)
#     else:
#         return n + 1
#
#
# answer = f(6)
# print(answer)
