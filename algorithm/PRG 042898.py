DIV_ = 1000000007


def solution(M_, N_, lst_puddle):
    grd_ = [[1 for _ in range(M_)] for _ in range(N_)]
    grd_[0][0] = 1
    for y_, x_ in lst_puddle:
        grd_[x_-1][y_-1] = 0

    idx_n = 0
    for idx_m in range(1, M_):
        if grd_[idx_n][idx_m]:
            grd_[idx_n][idx_m] = grd_[idx_n][idx_m - 1]

    for idx_n in range(1, N_):
        idx_m = 0
        if grd_[idx_n][idx_m]:
            grd_[idx_n][idx_m] = grd_[idx_n - 1][idx_m]
        for idx_m in range(1, M_):
            if grd_[idx_n][idx_m]:
                grd_[idx_n][idx_m] = grd_[idx_n - 1][idx_m] + grd_[idx_n][idx_m - 1]
                grd_[idx_n][idx_m] %= DIV_

    return grd_[-1][-1]
