import sys

M_, N_ = map(int, sys.stdin.readline().split())

grd_ = []

for _ in range(M_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

grd_dp = [[-1 for _ in range(N_)] for _ in range(M_)]
grd_dp[0][0] = 1
lst_offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def func_(idx_m, idx_n):
    if grd_dp[idx_m][idx_n] == -1:
        tot_ = 0
        for offset_m, offset_n in lst_offset:
            idx_target_m, idx_target_n = idx_m + offset_m, idx_n + offset_n
            if 0 <= idx_target_m < M_ \
                    and 0 <= idx_target_n < N_ \
                    and grd_[idx_target_m][idx_target_n] > grd_[idx_m][idx_n]:
                tot_ += func_(idx_target_m, idx_target_n)
        grd_dp[idx_m][idx_n] = tot_
    return grd_dp[idx_m][idx_n]


print(func_(M_ - 1, N_ - 1))

for each_ in grd_dp:
    print(each_)
print()
exit()
