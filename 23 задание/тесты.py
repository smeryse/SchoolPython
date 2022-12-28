def f(n, finish):
    if n == finish:
        return 1
    if n > finish or n == 31:
        return 0
    return f(n + 1, finish) + f(n * 2, finish)

print(f(2, 35))
