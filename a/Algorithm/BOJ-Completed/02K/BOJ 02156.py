import sys

lst_dp = [0, 0, 0]

for _ in range(int(sys.stdin.readline())):
    temp_ = int(sys.stdin.readline())
    lst_dp = [max(lst_dp), max(lst_dp[0], lst_dp[2]) + temp_, lst_dp[0] + temp_]

print(max(lst_dp))

exit()
