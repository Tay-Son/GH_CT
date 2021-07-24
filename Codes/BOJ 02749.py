import sys

n = int(sys.stdin.readline())
divider_ = 1000000
period_ = divider_ // 10 * 15

lst_dp = [0, 1]
for _ in range(2, period_):
    lst_dp.append((lst_dp[-1] + lst_dp[-2]) % divider_)

print(lst_dp[n % period_])