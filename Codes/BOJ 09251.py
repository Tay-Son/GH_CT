import sys

str_a = sys.stdin.readline().rstrip()
str_b = sys.stdin.readline().rstrip()

lst_dp = [0 for _ in range(len(str_a))]

for chr_ in str_b:
    max_ = 0
    lst_temp = []

    for idx_a in range(len(str_a)):
        if str_a[idx_a] == chr_:
            lst_temp.append(max_ + 1)
        else:
            lst_temp.append(lst_dp[idx_a])
        max_ = max(max_, lst_dp[idx_a])
    lst_dp = lst_temp

print(max(lst_dp))
exit()
