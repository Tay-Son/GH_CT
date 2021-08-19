import sys

D = int(sys.stdin.readline())
grp_ = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 7], [3, 4, 6], [5, 7], [4, 6]]
divider_ = 1000000007
lst_dp = [[1], [0], [0], [0], [0], [0], [0], [0]]

for cnt_d in range(D):
    for idx_ in range(8):
        tot_ = 0
        for idx_t in grp_[idx_]:
            tot_ += lst_dp[idx_t][cnt_d]
            tot_ %= divider_
        lst_dp[idx_].append(tot_)

print(lst_dp[0][D])