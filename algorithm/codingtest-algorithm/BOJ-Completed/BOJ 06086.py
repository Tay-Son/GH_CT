import sys
import string
from collections import deque

INF_ = 1001

dct_idx = {val_: idx_ for idx_, val_ in enumerate(string.ascii_letters)}
grd_cap = [[0 for _ in range(52)] for _ in range(52)]
grd_flw = [[0 for _ in range(52)] for _ in range(52)]

idx_src = dct_idx['A']
idx_snk = dct_idx['Z']

for _ in range(int(sys.stdin.readline())):
    a_, b_, w_ = sys.stdin.readline().split()
    a_, b_ = dct_idx[a_], dct_idx[b_]
    w_ = int(w_)
    grd_cap[a_][b_] += w_
    grd_cap[b_][a_] += w_

tot_ = 0
while True:
    lst_p = [-1 for _ in range(52)]
    lst_p[idx_src] = idx_src
    que_ = deque()
    que_.append(idx_src)
    while que_ and lst_p[idx_snk] == -1:
        idx_s = que_.popleft()
        for idx_e in range(52):
            if grd_cap[idx_s][idx_e] - grd_flw[idx_s][idx_e] > 0 and \
                    lst_p[idx_e] == -1:
                lst_p[idx_e] = idx_s
                que_.append(idx_e)

    if lst_p[idx_snk] == -1:
        break

    amount_ = INF_
    idx_s = idx_snk
    while idx_s != idx_src:
        idx_p = lst_p[idx_s]
        amount_ = min(amount_, grd_cap[idx_p][idx_s] - grd_flw[idx_p][idx_s])
        idx_s = idx_p

    idx_s = idx_snk
    while idx_s != idx_src:
        idx_p = lst_p[idx_s]
        grd_flw[idx_p][idx_s] += amount_
        grd_flw[idx_s][idx_p] -= amount_
        idx_s = idx_p
    tot_ += amount_

print(tot_)
exit()
