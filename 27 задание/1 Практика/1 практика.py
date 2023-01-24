def task_1(file_name):
    nums = []
    for row in list(open(file_name))[1:]:
        nums.append(tuple(map(lambda x: int(x), row.split())))


    max_sum = sum([max(num) for num in nums])
    dmin = min([abs(num[0] - num[1]) for num in nums if abs(num[0] - num[1]) % 3 != 0])

    if max_sum % 3 != 0:
        print(max_sum)
    else:
        print(max_sum - dmin)


def task_2(file_name):
    f = open(file_name).readlines()
    del f[0]
    s = 0
    dmin = 1000000000000
    for i in f:
        a, b = map(int, i.split())
        s += max(a, b)
        if abs(a - b) % 5 != 0:
            dmin = min(dmin, abs(a - b))
    if s % 5 != 0:
        print(s)
    else:
        print(s - dmin)


if __name__ == '__main__':
    task_2('file/2б.txt')