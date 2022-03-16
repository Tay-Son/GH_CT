import sys

R_, C_ = map(int, sys.stdin.readline().split())

grd_dp = []
for _ in range(R_):
    grd_dp.append(list(map(int, sys.stdin.readline().rstrip())))

max_ = grd_dp[0][0]
if not max_:
    for idx_r in range(1, R_):
        if grd_dp[idx_r][0]:
            max_ = 1
            break

if not max_:
    for idx_c in range(1, C_):
        if grd_dp[0][idx_c]:
            max_ = 1
            break

for idx_r in range(1, R_):
    for idx_c in range(1, C_):
        if grd_dp[idx_r][idx_c] == 1:
            grd_dp[idx_r][idx_c] = min(grd_dp[idx_r - 1][idx_c], grd_dp[idx_r][idx_c - 1],
                                       grd_dp[idx_r - 1][idx_c - 1]) + 1
        max_ = max(max_, grd_dp[idx_r][idx_c])

print(max_ * max_)
exit()

grd_dp = []
lst_temp = []
cnt_ = 0
for idx_c, value_ in enumerate(map(int, sys.stdin.readline().strip())):
    if value_:
        cnt_ += 1
    else:
        cnt_ = 0
    lst_temp.append([cnt_, value_])
grd_dp.append(lst_temp)

for idx_r in range(1, R_):
    lst_temp = []
    cnt_ = 0
    for idx_c, value_ in enumerate(map(int, sys.stdin.readline().strip())):
        if value_:
            cnt_ += 1
            value_ += grd_dp[idx_r - 1][idx_c][1]
        else:
            cnt_ = 0
        lst_temp.append([cnt_, value_])
        temp_ = min(cnt_, value_)

    grd_dp.append(lst_temp)

for each_ in grd_dp:
    print(each_)

max_ = 0
for idx_r in range(R_):
    offset_ = 0
    cnt_ = 1
    while idx_r + offset_ < R_ and offset_ < C_:
        print(idx_r + offset_, offset_, grd_dp[idx_r + offset_][offset_], cnt_)
        if min(grd_dp[idx_r + offset_][offset_]) >= cnt_:
            max_ = max(max_, cnt_ * cnt_)
            cnt_ += 1
        else:
            cnt_ = min(grd_dp[idx_r + offset_][offset_]) + 1
        offset_ += 1

for idx_c in range(1, C_):
    offset_ = 0
    cnt_ = 1
    while offset_ < R_ and idx_c + offset_ < C_:
        print(offset_, idx_c + offset_, grd_dp[offset_][idx_c + offset_], cnt_)
        if min(grd_dp[offset_][idx_c + offset_]) >= cnt_:
            max_ = max(max_, cnt_ * cnt_)
            cnt_ += 1
        else:
            cnt_ = min(grd_dp[offset_][idx_c + offset_]) + 1
        offset_ += 1

print(max_)

exit()
