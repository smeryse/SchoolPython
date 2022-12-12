N, M, n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(N)]


print(matrix)

nm = []

for i in range(N - n):
    for j in range(M - m):
        nm = 0
