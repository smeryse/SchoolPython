# 1
# def task(n):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = str(r) + '01'
#     else:
#         r = str(r) + '10'
#     return int(r, 2)
#
#
# num = 0
# for num in range(0, 10000):
#     if task(n=num) > 102:
#         print(task(n=num))
#         break


def task_2(num):
    r = bin(num)[2:-1]
    if num % 2 == 0:
        r = str(r) + '01'
    else:
        r = str(r) + '10'
    return int(r, 2)


2


# num = 0
# for num in range(0, 10000):
#     if task_3(num) == 2018:
#         print(num)
#         break

def task_3():
    for num in range(1, 100000):
        r = bin(num)[2:-1]
        if num % 2 == 0:
            r = str(r) + '01'
        else:
            r = str(r) + '10'
        if int(r, 2) == 2017:
            print(num)
            break


def task_4():
    for num in range(0, 256):
        r1 = bin(num)[2:]
        r2 = bin(num)[2:]
        r2 = r2.replace('1', '2')
        r2 = r2.replace('0', '1')
        r2 = r2.replace('2', '0')
        print(int(r2, 2) - int(r1, 2))



task_4()