import sys
from collections import deque

N_ = int(sys.stdin.readline())
mat_ = [[100, 70, 40, 0],
        [70, 50, 30, 0],
        [40, 30, 20, 0],
        [0, 0, 0, 0]]
dct_ = {'A': 0, 'B': 1, 'C': 2, 'F': 3}
grd_ = [[dct_[chr_] for chr_ in sys.stdin.readline().strip()] for _ in range(N_)]

grd_dp = [[-1 for _ in range(2 ** N_)] for _ in range(N_)]


def func_(bit_, depth_):
    if depth_ < 0:
        return 0
    else:
        if grd_dp[depth_][bit_] == -1:
            max_ = 0

            que_ = deque([(2 ** N_ - 1, 0, 0)])
            depth_t = depth_ - 1
            while que_:
                bit_c, idx_n, tot_ = que_.popleft()
                if idx_n == N_:
                    max_ = max(max_, tot_ + func_(bit_c, depth_t))
                else:
                    que_.append((bit_c, idx_n + 1, tot_))
                    if bit_ & 1 << idx_n:
                        if depth_ > 0:
                            val_a, val_b = grd_[depth_][idx_n], grd_[depth_t][idx_n]
                            que_.append((bit_c ^ 1 << idx_n, idx_n + 1, tot_ + mat_[val_a][val_b]))
                        if idx_n + 1 < N_ and bit_ & 1 << (idx_n + 1):
                            val_a, val_b = grd_[depth_][idx_n], grd_[depth_][idx_n + 1]
                            que_.append((bit_c, idx_n + 2, tot_ + mat_[val_a][val_b]))

            grd_dp[depth_][bit_] = max_
        return grd_dp[depth_][bit_]


max_ = 0
for bit_ in range(2 ** N_):
    max_ = max(max_, func_(bit_, N_ - 1))
print(max_)

for each_ in grd_dp:
    print(each_)
exit()


def rec_(bit_, idx_n):
    if grd_dp[idx_n][bit_] == -1:
        tot_ = 0
        que_ = deque([(2 ** M_ - 1, 0)])
        idx_t = idx_n - 1
        while que_:
            bit_c, idx_m = que_.popleft()
            if idx_m == M_:
                tot_ += rec_(bit_c, idx_t)
                tot_ %= DIV_
            else:
                if not bit_ & 1 << idx_m:
                    que_.append((bit_c, idx_m + 1))
                else:
                    que_.append((bit_c ^ 1 << idx_m, idx_m + 1))

                    if idx_m + 1 < M_ and bit_ & 1 << (idx_m + 1):
                        que_.append((bit_c, idx_m + 2))

        grd_dp[idx_n][bit_] = tot_
    return grd_dp[idx_n][bit_]
