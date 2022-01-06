import sys
from itertools import combinations as cb

N_, M_ = map(int, sys.stdin.readline().split())

grd_ = []
lst_house = []
lst_chick = []
for idx_c in range(N_):
    lst_temp = list(map(int, sys.stdin.readline().split()))
    for idx_r, value_ in enumerate(lst_temp):
        if value_ == 1:
            lst_house.append((idx_c, idx_r))
        elif value_ == 2:
            lst_chick.append((idx_c, idx_r))
    grd_.append(lst_temp)

grd_dist = []
for h_c, h_r in lst_house:
    lst_temp = []
    idx_chick = 0
    for c_c, c_r in lst_chick:
        lst_temp.append((abs(h_c - c_c) + abs(h_r - c_r), idx_chick))
        idx_chick += 1
    lst_temp.sort()
    grd_dist.append(lst_temp)

min_ = 1000000009
for cb_ in cb(range(len(lst_chick)), M_):
    set_cb = set(cb_)
    tot_ = 0
    for lst_dist in grd_dist:
        for dist_, idx_ in lst_dist:
            if idx_ in set_cb:
                tot_ += dist_
                break
    min_ = min(min_, tot_)

print(min_)

exit()
