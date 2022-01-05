import sys
from itertools import combinations as cb

N_, M_ = map(int, sys.stdin.readline().split())
mat_ = [[False for _ in range(N_ + 1)] for _ in range(N_ + 1)]

que_ = []
lst_ = [False for _ in range(N_ + 1)]
for idx_ in list(map(int, sys.stdin.readline().split()))[1:]:
    lst_[idx_] = True
    que_.append(idx_)

grd_ = []
for _ in range(M_):
    lst_temp = list(map(int, sys.stdin.readline().split()))[1:]
    for idx_a, idx_b in cb(lst_temp, 2):
        mat_[idx_a][idx_b] = True
        mat_[idx_b][idx_a] = True

    grd_.append(lst_temp)

idx_que = 0
while idx_que < len(que_):
    for idx_ in range(N_ + 1):
        if mat_[que_[idx_que]][idx_] == True and not lst_[idx_]:
            lst_[idx_] = True
            que_.append(idx_)
    idx_que += 1

tot_ = 0
for each_lst in grd_:
    is_ = True
    for each_ in each_lst:
        if lst_[each_]:
            is_ = False
            break
    if is_:
        tot_ += 1

print(tot_)

exit()
