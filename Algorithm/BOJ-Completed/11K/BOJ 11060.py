import sys

N_ = int(sys.stdin.readline())
lst_jmp = list(map(int, sys.stdin.readline().split()))
lst_dp = [-1 for _ in range(N_)]
lst_dp[N_ - 1] = 0

for idx_ in range(N_ - 2, -1, -1):
    if idx_ + lst_jmp[idx_] >= N_ - 1:
        lst_dp[idx_] = 1
    else:
        min_ = 10 ** 4
        for idx_target in range(idx_ + 1, min(idx_ + 1 + lst_jmp[idx_], N_)):
            temp_ = lst_dp[idx_target]
            if temp_ != -1:
                min_ = min(min_, temp_ + 1)
        if min_ != 10 ** 4:
            lst_dp[idx_] = min_

print(lst_dp[0])

exit()
