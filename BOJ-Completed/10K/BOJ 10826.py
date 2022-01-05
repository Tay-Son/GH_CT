import sys

n = int(sys.stdin.readline())

lst_dp = [0,1]
if n>1:
    for _ in range(2,n+1):
        lst_dp.append(lst_dp[-1]+lst_dp[-2])

print(lst_dp[n])