import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

lst_dp = [0]
for idx_ in range(0, N_):
    lst_dp.append(max(map(lambda x: lst_[x] + lst_dp[idx_ - x], range(idx_ + 1))))

print(lst_dp[-1])

exit()