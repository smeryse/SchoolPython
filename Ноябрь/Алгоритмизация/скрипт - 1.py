def task_1(n=0):
    r = str(bin(n)[2:])
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    return int(r, 2)


def task_1_1():
    n = int(input())
    r = bin(n)[2:]
    r = str(r)
    if r.count('1') % 2 == 1:
        r = r + '1'
    else:
        r = r + '0'
    if r.count('1') % 2 == 1:
        r = r + '1'
    else:
        r = r + '0'
    print(int(r, 2))


def task_3(num):
    r = bin(num)[2:]
    r += str(num % 2) * 2
    return int(r)


c = 0
for i in range(100, 1000):
    n = i
    n1 = int(str(n)[0])
    n2 = int(str(n)[1])
    n3 = int(str(n)[2])
    s1 = n1 + n2
    s2 = n2 + n3
    r = str(max(s1, s2)) + str(min(s1, s2))
    if r == '1715':
        c += 1
print(c)

# num = int(input('Your num: '))
#
# for i in range(0, 10**10):
#     if task_3(i) > num:
#         print(i)
#         break

