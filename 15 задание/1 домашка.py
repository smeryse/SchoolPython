# task_1
# def DEL(n, m):
#     if n % m == 0:
#         return True
#     else:
#         return False
#
#
# def f(A, x):
#     return DEL(144, A) and ((not DEL(x, A)) <= (DEL(x, 18) <= (not DEL(x, 24))))
#
#
# for A in range(1, 10000):
#     if all(f(A, x) for x in range(1, 500)):
#         print(A)

# answer = 72

# task_2
# def DEL(n, m):
#     return n % m == 0
#
#
# def f(A, x):
#     return DEL(70, A) and ((not DEL(x, A)) <= (DEL(x, 35) <= (not DEL(x, 63))))
#
#
# for A in range(1, 500):
#     if all(f(A, x) for x in range(1, 500)):
#         print(A)


# answer = 35

# task_3
# def f(A, x, y):
#     return  (x * y < 140) or (y > A) or (x > A)
#
# for A in range(10000):
#     if all(f(A, x, y) for x in range(500) for y in range(500)):
#         print(A)

# answer = 11

# task_4
# def f(A, x, y):
#     return (2 * x + 3 * y < A) or (x > y) or (y > 24)
#
#
# for A in range(1000):
#     if all(f(A, x, y) for x in range(500) for y in range(500)):
#         print(A)
#         break

# answer = 121

# task_5
# def f(A, x):
#     return ((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & A != 0))
#
#
# for A in range(500):
#     if all(f(A, x) for x in range(500)):
#         print(A)
#         break

# answer = 13

# task_6
# def f(A, x):
#     return x & 51 == 0 or (x & 41 == 0 <= x & A == 0)
#
#
# for A in range(1000):
#     if all(f(A, x) for x in range(500)):
#         print(A)
#         break

# answer = 0
