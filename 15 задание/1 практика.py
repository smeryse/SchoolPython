# task_3
# def f(A, x, y):
#     return (y + 2 * x < A) or (x > 30) or (y > 20)
#
# for A in range(500):
#     if all(f(A, x, y) for x in range(500) for y in range(500)):
#         print(A)
#         break
#
# answer = 81

# task_4
# def f(A, x, y):
#     return (y + 2 * x != 48) or (A < x) or (x < y)
#
#
# for A in range(1000):
#     if all(f(A, x, y) for x in range(500) for y in range(500)):
#         print(A)

# answer = 15

# task_5
# def f(A, x):
#     return ((x & 29) != 0) <= ((x & 17 == 0) <= ((x & A) != 0))
#
#
# for A in range(1000):
#     if all(f(A, x) for x in range(500)):
#         print(A)

# answer = 12

# task_6
# def f(A, x):
#     return ((x & 25) != 0) <= (((x & 17) == 0) <= ((x & A) != 0))
#
# for A in range(500):
#     if all(f(A, x) for x in range(500)):
#         print(A)

# answer = 8

# task_7
# def f(A, x):
#     return ((x & 25) != 0) <= (((x & 9) == 0) <= ((x & A) != 0))
#
# for A in range(500):
#     if all(f(A, x) for x in range(500)):
#         print(A)
#         break

# answer = 16

# task_8
# def dels(n, m):
#     if n % m == 0:
#         return True
#     else:
#         return False
#
# for A in range(1, 500):
#     flag = True
#     for x in range(500):
#         if (not (dels(x, A))) <= (dels(x, 6)) <= (not (dels(x, 4))):
#             print(A)
#         else:
#             Flag = False
#             break
#     if flag:
#         print(A)
# answer = 12
