n = 3
steps = [[1, 1], [3, 2], [2, 5]]

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(1, n):
    xx, yy = abs(steps[i][0] - steps[i-1][0]), abs(steps[i][1] - steps[i-1][1])
    if not(1 <= xx <= 2) or not(1 <= yy <= 2):
        err = i
        print(err)
        break

rx = steps[err][0] - steps[err - 1][0]
ry = steps[err][1] - steps[err - 1][1]

def recurs():
    for i in range(8):
        for j in range(8):
            if rx == dx[i] + dx[j] and ry == dy[i] + dy[j]:
                result = steps[err-1][0] + dx[i], steps[err-1][1] + dy[i]
                return result

print(*recurs())