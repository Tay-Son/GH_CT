import sys

for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    lst_dp = [0 for _ in range(N_ + 1)]
    lst_dp[0] = 1
    if N_ > 0:
        lst_dp[1] = lst_dp[0]
    if N_ > 1:
        lst_dp[2] = lst_dp[0] + lst_dp[1]
    if N_ > 2:
        for idx_ in range(3, N_ + 1):
            lst_dp[idx_] = lst_dp[idx_ - 1] + \
                           lst_dp[idx_ - 2] + \
                           lst_dp[idx_ - 3]
    print(lst_dp[N_])

exit()
