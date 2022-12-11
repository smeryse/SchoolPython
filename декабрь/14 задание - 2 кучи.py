def f(s, n, m):
    if s >= 69:
        return n % 2 == m % 2

    if n == m:
        return False
    h = [f(s + 1, n + 1, m),
         f(s + 4, n + 1, m),
         f(s * 5, n + 1, m)]

    if (n + 1) % 2 == m % 2:
        return any(h)
    else:
        return all(h)


# for s in range(1, 69):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             print(s, m)
#             break


# def f2(k1, k2, step, my_step):
#     if k1 + k2 >= 77:
#         return step % 2 == my_step % 2
#     if step == my_step:
#         return False
#     steps = [
#         f2(k1 + 1, k2, step + 1, my_step),
#         f2(k1 * 2, k2, step + 1, my_step),
#         f2(k1, k2 + 1, step + 1, my_step),
#         f2(k1, k2 * 2, step + 1, my_step)
#     ]
#     if (step + 1) % 2 == my_step % 2:
#         return any(steps)
#     else:
#         return all(steps)
#
#
# for stone in range(1, 70):
#     for my_step in range(1, 5):
#         if f2(7, stone, 0, my_step):
#             print(stone + 7, my_step)


def f2(k1, k2, step, my_step):
    if k1 + k2 >= 74:
        return step % 2 == my_step % 2
    if step == my_step:
        return False
    steps = [
        f2(k1 + 1, k2, step + 1, my_step),
        f2(k1, k2 + 1, step + 1, my_step),
        f2(k1 * 2, k2, step + 1, my_step),
        f2(k1, k2 * 2, step + 1, my_step)
    ]
    if (step + 1) % 2 == my_step % 2:
        return any(steps)
    else:
        return all(steps)

# for stone in range(1, 62):
#     for step in range(1, 5):
#         if f2(stone, 12, 0, step):
#             print(stone, step)
#             break