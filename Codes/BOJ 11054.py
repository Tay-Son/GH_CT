import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

lst_dp = [[0, 0] for _ in range(N_)]
for idx_ in range(N_):
    idx_inverted = N_ - 1 - idx_

    max_ = 0
    for idx_sub in range(idx_):
        if lst_[idx_sub] < lst_[idx_]:
            max_ = max(max_, lst_dp[idx_sub][0])
    lst_dp[idx_][0] = max_ + 1

    max_ = 0
    for idx_sub in range(N_ - 1, idx_inverted, -1):
        if lst_[idx_sub] < lst_[idx_inverted]:
            max_ = max(max_, lst_dp[idx_sub][1])
    lst_dp[idx_inverted][1] = max_ + 1

print(max(map(lambda x: sum(x) - 1, lst_dp)))

exit()
