import sys

N_ = int(sys.stdin.readline())

r_0, g_0, b_0 = map(int, sys.stdin.readline().split())
r_1, g_1, b_1 = map(int, sys.stdin.readline().split())

if N_ <= 2:
    print(min(r_0 + g_1, r_0 + b_1, g_0 + r_1, g_0 + b_1, b_0 + r_1, b_0 + g_1))
else:
    r_2, g_2, b_2 = map(int, sys.stdin.readline().split())

    grd_ = [[min(r_0 + g_1, r_0 + b_1) + r_2, r_0 + b_1 + g_2, r_0 + g_1 + b_2],
            [g_0 + b_1 + r_2, min(g_0 + r_1, g_0 + b_1) + g_2, g_0 + r_1 + b_2],
            [b_0 + g_1 + r_2, b_0 + r_1 + g_2, min(b_0 + r_1, b_0 + g_1) + b_2]]
    if N_ > 3:
        for _ in range(3, N_):
            r_, g_, b_ = map(int, sys.stdin.readline().split())
            for idx_ in range(3):
                lst_temp = [r_, g_, b_]
                lst_temp[0] += min(grd_[idx_][1], grd_[idx_][2])
                lst_temp[1] += min(grd_[idx_][0], grd_[idx_][2])
                lst_temp[2] += min(grd_[idx_][0], grd_[idx_][1])
                grd_[idx_] = lst_temp

    print(min(grd_[0][1], grd_[0][2], grd_[1][0], grd_[1][2], grd_[2][0], grd_[2][1]))

exit()
