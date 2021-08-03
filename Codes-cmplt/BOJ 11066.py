import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] + a
    d = [[987654321] * n for _ in range(n)]
    v = [[0] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
        v[i][i] = i
        s[i + 1] += s[i]
    for k in range(1, n):
        for j in range(k, n):
            i = j - k
            for l in range(v[i][j - 1], min(v[i + 1][j] + 1, j)):
                if d[i][l] + d[l + 1][j] < d[i][j]:
                    d[i][j] = d[i][l] + d[l + 1][j]
                    v[i][j] = l
            d[i][j] += s[j + 1] - s[i]
    print(d[0][n - 1])