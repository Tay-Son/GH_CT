import sys

N_,K_ = map(int,sys.stdin.readline().split())

exit()


import sys

N, K = map(int, sys.stdin.readline().split())
lst_w = [0]
lst_v = [0]
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    lst_w.append(w)
    lst_v.append(v)

grd_dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for rng_ in range(1, N + 1):
    for idx_w in range(K + 1):
        max_ = 0
        if idx_w - lst_w[rng_] >= 0:
            max_ = max(max_, lst_v[rng_] + grd_dp[rng_-1][idx_w-lst_w[rng_]])
        grd_dp[rng_][idx_w] = max(max_,grd_dp[rng_-1][idx_w])

print(grd_dp[-1][-1])