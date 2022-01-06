import sys

N = int(sys.stdin.readline())
lst_dp = [0 for _ in range(N + 1)]
lst_dp[0] = 0
lst_dp[1] = 1

if N > 1:
    lst_dp[2] = 2
if N > 2:
    for idx_ in range(3, N + 1):
        lst_dp[idx_] = (lst_dp[idx_ - 1] + lst_dp[idx_ - 2]) % 15746

print(lst_dp[N])