import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

lst_dp = [lst_[0]]
for idx_ in range(1, N_):
    max_ = 0
    for idx_sub in range(idx_):
        if lst_[idx_sub] < lst_[idx_]:
            max_ = max(max_, lst_dp[idx_sub])
    lst_dp.append(max_ + lst_[idx_])
print(max(lst_dp))

exit()
