import sys

N_ = int(sys.stdin.readline())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().split())))


def rec_(mag_, idx_s_n, idx_s_m):
    if mag_ > 1:

        tot_w = 0
        tot_b = 0
        mag_ //= 2

        temp_w, temp_b = rec_(mag_, idx_s_n, idx_s_m)
        tot_w += temp_w
        tot_b += temp_b
        temp_w, temp_b = rec_(mag_, idx_s_n + mag_, idx_s_m)
        tot_w += temp_w
        tot_b += temp_b
        temp_w, temp_b = rec_(mag_, idx_s_n, idx_s_m + mag_)
        tot_w += temp_w
        tot_b += temp_b
        temp_w, temp_b = rec_(mag_, idx_s_n + mag_, idx_s_m + mag_)
        tot_w += temp_w
        tot_b += temp_b

        if tot_w == 4 and tot_b == 0:
            return (1, 0)
        elif tot_b == 4 and tot_w == 0:
            return (0, 1)
        else:
            return (tot_w, tot_b)
    else:
        if grd_[idx_s_n][idx_s_m]:
            return (0, 1)
        else:
            return (1, 0)


for each_ in rec_(N_, 0, 0):
    print(each_)

exit()
