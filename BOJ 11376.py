import sys

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(2 * N_ + 1)]
lst_d = [0 for _ in range(M_)]
for idx_n in range(N_):
    lst_input = list(map(int, sys.stdin.readline().split()))
    for idx_m in map(lambda x: int(x) - 1, lst_input[1:]):
        grp_[2 * idx_n + 1].append(idx_m)
        grp_[2 * idx_n + 2].append(idx_m)

for each_ in grp_:
    print(each_)


def func(idx_n):
    if lst_visited[idx_n]:
        return False
    else:
        lst_visited[idx_n] = True
        for idx_m in grp_[idx_n]:
            if lst_d[idx_m] == 0 or func(lst_d[idx_m]):
                lst_d[idx_m] = idx_n
                return True
        return False


answer_ = 0
for idx_n in range(1, 2 * N_ + 1):
    lst_visited = [False for _ in range(2 * N_ + 1)]
    if func(idx_n):
        answer_ += 1

print(answer_)

exit()

import sys

from collections import deque

N_, M_ = map(int, sys.stdin.readline().split())
C_ = N_ + M_ + 2

grd_cap = [[0 for _ in range(C_)] for _ in range(C_)]
grd_flw = [[0 for _ in range(C_)] for _ in range(C_)]

idx_src = 0
idx_snk = C_ - 1

for idx_n in range(1, N_ + 1):
    lst_temp = sys.stdin.readline().split()
    K_ = int(lst_temp[0])
    grd_cap[idx_src][idx_n] = K_
    grd_cap[idx_n][idx_src] = K_
    for idx_m in map(lambda x: int(x) + N_, lst_temp[1:]):
        grd_cap[idx_n][idx_m] = 1
        grd_cap[idx_m][idx_n] = 1

for idx_m in range(N_ + 1, C_ - 1):
    grd_cap[idx_m][idx_snk] = 1
    grd_cap[idx_snk][idx_m] = 1

for each_ in grd_cap:
    print(each_)
print()

tot_ = 0
while True:
    que_ = deque()
    que_.append(idx_src)
    lst_p = [-1 for _ in range(C_)]
    lst_p[idx_src] = idx_src
    while que_ and lst_p[idx_snk] == -1:
        idx_n = que_.popleft()
        for idx_m in range(C_):
            if lst_p[idx_m] == -1 and grd_cap[idx_n][idx_m] - grd_flw[idx_n][idx_m] > 0:
                lst_p[idx_m] = idx_n
                que_.append(idx_m)

    if lst_p[idx_snk] == -1:
        break

    amount_ = 1000
    idx_s = idx_snk
    while idx_s != idx_src:
        idx_p = lst_p[idx_s]
        amount_ = min(amount_, grd_cap[idx_p][idx_s] - grd_flw[idx_p][idx_s])
        idx_s = idx_p

    print(amount_, lst_p)
    idx_s = idx_snk
    while idx_s != idx_src:
        idx_p = lst_p[idx_s]
        grd_flw[idx_s][idx_p] -= amount_
        grd_flw[idx_p][idx_s] += amount_
        idx_s = idx_p
    tot_ += amount_

print()
for each_ in grd_cap:
    print(each_)
print()
for each_ in grd_flw:
    print(each_)
print()

print(tot_)
exit()
