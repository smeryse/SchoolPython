n, a, b = [int(i) for i in input().split()]
ab = list(range(b, a - 1, -1))


count = 0
for kg in ab:
    x = n // kg
    count += x
    n -= x * kg


print(count)