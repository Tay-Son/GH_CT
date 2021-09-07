import sys

n, k = map(int, sys.stdin.readline().split())
lst_n = [0 for _ in range(n + 1)]
for idx_n in range(1, n + 1):
    lst_n[idx_n] = int(sys.stdin.readline())

lst_dp = [0 for _ in range(k + 1)]
lst_dp[0] = 1

for idx_n in range(1, n + 1):
    for idx_k in range(lst_n[idx_n], k + 1):
        lst_dp[idx_k] += lst_dp[idx_k - lst_n[idx_n]]

print(lst_dp[-1])

exit()
