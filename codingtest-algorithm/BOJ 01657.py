import sys

N_, M_ = map(int, sys.stdin.readline().split())

dct_ = {val_: idx_ for idx_, val_ in enumerate('ABCDF')}
mat_ = [[10, 8, 7, 5, 1],
        [8, 6, 4, 3, 1],
        [7, 4, 3, 2, 1],
        [5, 3, 2, 2, 1],
        [1, 1, 1, 1, 0]]

grd_ = [list(map(lambda x: dct_[x], sys.stdin.readline().strip())) for _ in range(N_)]
grd_dp = [[[-1 for _ in range(2 ** M_)] for _ in range(M_)] for _ in range(N_)]


def rec_(idx_n, idx_m, bit_):
    if idx_m == M_:
        idx_n += 1
        idx_m = 0

    if idx_n == N_:
        return 0
    else:
        if grd_dp[idx_n][idx_m][bit_] == -1:
            if bit_ & 1 == 1:
                grd_dp[idx_n][idx_m][bit_] = rec_(idx_n, idx_m + 1, bit_ >> 1)
            else:
                max_ = 0
                if idx_m < M_ - 1 and bit_ & 2 == 0:
                    val_a, val_b = grd_[idx_n][idx_m], grd_[idx_n][idx_m + 1]
                    max_ = max(max_,
                               rec_(idx_n, idx_m + 1, (bit_ >> 1) | 1) + mat_[val_a][val_b])

                if idx_n < N_ - 1 and bit_ & (1 << M_) == 0:
                    val_a, val_b = grd_[idx_n][idx_m], grd_[idx_n + 1][idx_m]
                    max_ = max(max_,
                               rec_(idx_n, idx_m + 1, (bit_ | (1 << M_)) >> 1) + mat_[val_a][val_b])

                max_ = max(max_,
                           rec_(idx_n, idx_m + 1, bit_ >> 1))

                grd_dp[idx_n][idx_m][bit_] = max_
        return grd_dp[idx_n][idx_m][bit_]


print(rec_(0, 0, 0))
exit()

