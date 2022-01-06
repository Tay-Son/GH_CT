import sys

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    lst_.append(tuple(map(int, sys.stdin.readline().split())))

lst_dp = [0 for _ in range(N_ + 1)]
for idx_ in range(N_ - 1, -1, -1):
    estm_, prft_ = lst_[idx_]
    lst_dp[idx_] = lst_dp[idx_ + 1]
    temp_ = idx_ + estm_
    if temp_ <= N_:
        lst_dp[idx_] = max(lst_dp[idx_], prft_ + lst_dp[temp_])

print(lst_dp[0])
exit()