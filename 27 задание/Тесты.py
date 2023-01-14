A = {file.replace('\n', '') for file in open('27-A.txt').readlines()}
B = {file.replace('\n', '') for file in open('27-B.txt').readlines()}

# codes here
sums = []
for num1 in A:
    _A = A - {num1}
    for num2 in _A:
        __A = _A - {num2}
        for num3 in A:
            s = int(num2) + int(num2) + int(num3)
            if s % 3 == 0:
                sums.append(s)


print(max(sums))