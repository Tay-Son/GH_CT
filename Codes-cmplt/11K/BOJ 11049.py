import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
times = [[0 for i in range(n)] for j in range(n)]
for i in range(n - 1):
    times[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]
for j in range(2, n):
    for i in range(j - 2, -1, -1):
        inf = times[i][j - 1] + matrix[i][0] * matrix[j][0] * matrix[j][1]
        for k in range(i, j - 1):
            z = times[i][k] + times[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            if inf > z:
                inf = z
        times[i][j] = inf
print(times[0][n - 1])
