import sys

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    a_, b_ = map(int, sys.stdin.readline().split())
    lst_.append((a_, b_))

lst_ = [tup_[1] for tup_ in sorted(lst_, key=lambda x: x[0])]
lst_dp = [1]
for idx_ in range(1, N_):
    max_ = 1
    for idx_sub in range(idx_):
        if lst_[idx_] > lst_[idx_sub]:
            max_ = max(max_, lst_dp[idx_sub] + 1)
    lst_dp.append(max_)

print(lst_dp)

print(N_ - max(lst_dp))

exit()
