import sys

DIV_ = 1000000000

N_ = int(sys.stdin.readline())
lst_dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if N_ > 1:
    for _ in range(1, N_):
        lst_temp = [lst_dp[1]]
        for idx_ in range(1, 9):
            lst_temp.append((lst_dp[idx_ - 1] + lst_dp[idx_ + 1]) % DIV_)
        lst_temp.append(lst_dp[8])
        lst_dp = lst_temp
print(sum(lst_dp) % DIV_)
