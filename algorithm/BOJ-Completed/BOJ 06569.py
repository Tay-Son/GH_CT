import sys
from collections import deque


def rec_(bit_, idx_n, grd_dp, M_):
    if grd_dp[idx_n][bit_] == -1:
        tot_ = 0
        que_ = deque([(2 ** M_ - 1, 0)])
        idx_t = idx_n - 1
        while que_:
            bit_c, idx_m = que_.popleft()
            if idx_m == M_:
                tot_ += rec_(bit_c, idx_t, grd_dp, M_)
            else:
                if not bit_ & 1 << idx_m:
                    que_.append((bit_c, idx_m + 1))
                else:
                    que_.append((bit_c ^ 1 << idx_m, idx_m + 1))

                    if idx_m + 1 < M_ and bit_ & 1 << (idx_m + 1):
                        que_.append((bit_c, idx_m + 2))

        grd_dp[idx_n][bit_] = tot_
    return grd_dp[idx_n][bit_]


R_, C_ = map(int, sys.stdin.readline().split())
while R_ + C_:
    N_, M_ = min(R_, C_), max(R_, C_)
    grd_dp = [[0 for _ in range(2 ** M_ - 1)] + [1]] + [[-1 for _ in range(2 ** M_)] for _ in range(N_)]

    print(rec_(2 ** M_ - 1, N_, grd_dp, M_))

    R_, C_ = map(int, sys.stdin.readline().split())

exit()
