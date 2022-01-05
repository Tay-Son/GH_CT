import sys
from itertools import combinations as cb

N_, M_ = map(int, sys.stdin.readline().split())
grd_ = []
lst_gas = []
lst_empty = []
for idx_n in range(N_):
    lst_temp = list(map(int, sys.stdin.readline().split()))
    for idx_m, each_ in enumerate(lst_temp):
        if each_ == 0:
            lst_empty.append((idx_n, idx_m))
        elif each_ == 2:
            lst_gas.append((idx_n, idx_m))
    grd_.append(lst_temp)


def dfs_(idx_s_n, idx_s_m, grd_iv):
    grd_iv[idx_s_n][idx_s_m] = True
    tot_ = 1
    for o_n, o_m in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        t_n, t_m = idx_s_n + o_n, idx_s_m + o_m
        if 0 <= t_n < N_ and 0 <= t_m < M_ and not grd_iv[t_n][t_m] and grd_[t_n][t_m] != 1:
            tot_ += dfs_(t_n, t_m, grd_iv)
    return tot_


max_ = 0
for cb_ in cb(lst_empty, 3):
    for idx_n, idx_m in cb_:
        grd_[idx_n][idx_m] = 1

    grd_iv = [[False for _ in range(M_)] for _ in range(N_)]
    tot_ = 0
    for idx_s_n, idx_s_m in lst_gas:
        if not grd_iv[idx_s_n][idx_s_m]:
            tot_ += dfs_(idx_s_n, idx_s_m, grd_iv)

    max_ = max(max_, len(lst_empty) - tot_ - 3 + len(lst_gas))

    for idx_n, idx_m in cb_:
        grd_[idx_n][idx_m] = 0

print(max_)

exit()
