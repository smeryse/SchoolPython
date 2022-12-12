#task_1
# def f(n):
#     if n <= 1:
#         return 1
#     elif n % 2 == 0 and n > 1:
#         return n + f(n-1)
#     elif n % 2 == 1 and n > 1:
#         return n*n + f(n-2)
#
# print(f(82))
# answer = 91963

# task_2
# def f(n):
#     if n <= 1:
#         return 1
#     elif n % 2 == 0 and n > 1:
#         return n * f(n-1)
#     elif n % 2 == 1 and n > 1:
#         return n + f(n-2)
#
# print(f(84))
# answer = 148176

# # task_4
# def f(n):
#     if n <= 3:
#         return n
#     elif n > 3 and n % 2 == 0:
#         return 2 * n + f(n - 1)
#     elif n > 3 and n % 2 == 1:
#         return n ** 2 + f(n - 2)
#
# count = 0
# for n in range(1, 101):
#     if f(n) % 3 == 0:
#         count += 1
#
# print(count)
# answer = 32

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
# answer = 32

# task_4
# def f(n):
#     if n <= 10:
#         return n
#     elif 10 < n <= 36:
#         return n // 4 + f(n - 10)
#     elif n > 36:
#         return 2 * f(n - 5)
#
# print(f(100))
# answer = 180224

# task_5
# def f(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return f(n - 1) + 3 * g(n - 1)
#
#
# def g(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return f(n - 1) - 2 * g(n - 1)
#
# answer = list(str(f(18)))
# print(sum([int(i) for i in answer]))
# answer = 46

# task_6
#
# ff = [0] * 37
# gg = [0] * 37
#
# def f(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return f(n - 1) - 2 * g(n - 1)
#
#
# def g(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return f(n - 1) + g(n - 1) + n
#
#
# for n in range(1, 11):
#     ff[n] = f(n)
#     gg[n] = g(n)
#
# for n in range(11, 37):
#     ff[n] = ff[n - 1] - 2 * gg[n - 1]
#     gg[n] = ff[n - 1] + gg[n - 1] + n
#
# print(gg)
# answer = 270918534

# task_7
# def f(n):
#     if n < 2:
#         return 1
#     elif n >= 2 and n % 2 == 0:
#         return f(n / 2) + 1
#     elif n >= 2 and n % 2 == 1:
#         return  f(n - 3) + 3
#
# count = 0
# for n in range(1, 10001):
#     if f(n) == 12:
#         count += 1
#
# print(count)
# result = 26

