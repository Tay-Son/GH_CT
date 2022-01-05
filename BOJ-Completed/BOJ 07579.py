import sys

N_, M_ = map(int, sys.stdin.readline().split())
lst_b = list(map(int, sys.stdin.readline().split()))
lst_c = list(map(int, sys.stdin.readline().split()))

sum_c = sum(lst_c)
min_ = sum_c
lst_dp = [0 for _ in range(sum_c + 1)]

for b_, c_ in zip(lst_b, lst_c):
    lst_temp = []
    for idx_c in range(0, sum_c + 1):
        if idx_c >= c_:
            lst_temp.append(max(b_ + lst_dp[idx_c - c_], lst_dp[idx_c]))
        else:
            lst_temp.append(lst_dp[idx_c])

        if lst_temp[-1] >= M_:
            min_ = min(min_, idx_c)
    lst_dp = lst_temp

print(min_)

exit()
