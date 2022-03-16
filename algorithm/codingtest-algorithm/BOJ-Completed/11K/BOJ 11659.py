import sys

N, M = map(int, sys.stdin.readline().split())

lst_ = list(map(int, sys.stdin.readline().split()))
lst_dp = [0]
tot_ = 0

for idx_ in range(N):
    tot_ += lst_[idx_]
    lst_dp.append(tot_)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(lst_dp[j] - lst_dp[i - 1])