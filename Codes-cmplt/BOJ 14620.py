import sys
from itertools import combinations as cb

lst_aux = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

N_ = int(sys.stdin.readline())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

grd_dp = [[0 for _ in range(N_ - 2)] for _ in range(N_ - 2)]
for idx_a in range(1, N_ - 1):
    for idx_b in range(1, N_ - 1):
        for aux_ in lst_aux:
            grd_dp[idx_a - 1][idx_b - 1] += grd_[idx_a + aux_[0]][idx_b + aux_[1]]

tot_min = 20000
for cb_ in cb(range((N_ - 2) ** 2), 3):
    lst_pos = []
    for each_ in cb_:
        lst_pos.append(list(divmod(each_, N_ - 2)))

    is_ = True
    for cb2_ in cb(range(3), 2):
        diff_a = abs(lst_pos[cb2_[0]][0] - lst_pos[cb2_[1]][0])
        diff_b = abs(lst_pos[cb2_[0]][1] - lst_pos[cb2_[1]][1])
        if diff_a + diff_b <= 2:
            is_ = False
            break

    if is_:
        tot_ = 0
        for pos_ in lst_pos:
            tot_ += grd_dp[pos_[0]][pos_[1]]
        tot_min = min(tot_min, tot_)
print(tot_min)

exit()