import sys

N_, M_ = map(int, sys.stdin.readline().split())

grd_dp = [[0 for _ in range(N_ + 1)]]

for idx_r in range(N_):
    tot_ = 0
    lst_temp = [0]
    for idx_c, value_ in enumerate(map(int, sys.stdin.readline().split())):
        tot_ += value_
        lst_temp.append(tot_ + grd_dp[idx_r][idx_c + 1])
    grd_dp.append((lst_temp))

for _ in range(M_):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1 = x1 - 1, y1 - 1
    print(grd_dp[x2][y2] - grd_dp[x2][y1] - grd_dp[x1][y2] + grd_dp[x1][y1])
exit()
