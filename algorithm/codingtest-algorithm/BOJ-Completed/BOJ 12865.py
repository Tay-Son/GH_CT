import sys

N_, K_ = map(int, sys.stdin.readline().split())
lst_W = []
lst_V = []
for _ in range(N_):
    W_, V_ = map(int, sys.stdin.readline().split())
    lst_W.append(W_)
    lst_V.append(V_)

lst_dp = [0 for _ in range(K_ + 1)]

for idx_ in range(N_):
    lst_temp = []
    for idx_w in range(K_ + 1):
        max_ = 0
        if idx_w >= lst_W[idx_]:
            lst_temp.append(max(lst_V[idx_] + lst_dp[idx_w - lst_W[idx_]], lst_dp[idx_w]))
        else:
            lst_temp.append(lst_dp[idx_w])
    lst_dp = lst_temp
print(lst_dp[-1])
exit()
