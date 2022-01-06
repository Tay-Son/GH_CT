import sys

N_ = int(sys.stdin.readline())
if N_ % 2:
    print(0)
else:
    N_ //= 2
    lst_dp = [1, 3]
    if N_ > 1:
        for _ in range(2, N_ + 1):
            lst_dp.append(lst_dp[-1] * 3 + sum(lst_dp[:-1]) * 2)
    print(lst_dp[-1])
exit()