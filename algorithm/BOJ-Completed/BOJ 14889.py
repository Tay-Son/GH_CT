import sys
from itertools import combinations as cb

N_ = int(sys.stdin.readline())
mat_ = []
for _ in range(N_):
    mat_.append(list(map(int, sys.stdin.readline().split())))

min_ = 20 * 20 * 100
for cb_ in cb(range(N_), N_ // 2):

    tot_s = 0
    tot_l = 0
    for idx_a in range(N_):
        for idx_b in range(N_):
            if idx_a in cb_:
                if idx_b in cb_:
                    tot_s += mat_[idx_a][idx_b]
            elif idx_b not in cb_:
                tot_l += mat_[idx_a][idx_b]
    min_ = min(min_, abs(tot_s - tot_l))
print(min_)

exit()