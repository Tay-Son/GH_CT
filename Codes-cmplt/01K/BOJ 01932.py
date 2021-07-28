import sys

N_ = int(sys.stdin.readline())
lst_dp = [int(sys.stdin.readline())]

for cnt_ in range(1, N_):
    lst_input = list(map(int, sys.stdin.readline().split()))
    lst_temp = [lst_dp[0] + lst_input[0]]
    for idx_ in range(1, cnt_):
        lst_temp.append(max(lst_dp[idx_ - 1], lst_dp[idx_]) + lst_input[idx_])
    lst_temp.append(lst_dp[-1] + lst_input[-1])
    lst_dp = lst_temp

print(max(lst_dp))

exit()
