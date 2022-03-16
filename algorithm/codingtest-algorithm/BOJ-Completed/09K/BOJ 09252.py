import sys

str_a = sys.stdin.readline().split()[0]
str_b = sys.stdin.readline().split()[0]
len_a = len(str_a)
len_b = len(str_b)
lst_dp = [[0 for _ in range(len_a)]]

lst_dp = [[]]

chr_b = str_b[0]
for chr_a in str_a:
    if chr_a == chr_b:
        lst_dp[0].append(1)
    else:
        lst_dp[0].append(0)

for chr_b in str_b[1:]:
    lst_temp = []
    max_ = 0
    cnt_ = 0
    for chr_a in str_a:
        if chr_a == chr_b:
            lst_temp.append(max_ + 1)
        else:
            lst_temp.append(lst_dp[-1][cnt_])
        max_ = max(max_, lst_dp[-1][cnt_])
        cnt_ += 1
    lst_dp.append(lst_temp)

answer_ = max(lst_dp[-1])
print(answer_)
if answer_:
    str_answer = ''
    idx_a = len_a - 1
    idx_b = len_b - 1
    for target_ in range(answer_, 0, -1):
        while lst_dp[idx_b][idx_a] != target_:
            idx_a -= 1
        while str_b[idx_b] != str_a[idx_a]:
            idx_b -= 1
        str_answer = str_a[idx_a] + str_answer
        idx_a -= 1
        idx_b -= 1
    print(str_answer)