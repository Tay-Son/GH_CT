import sys

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
max_ = 0
for _ in range(R_):
    lst_temp = list(map(int, sys.stdin.readline().rstrip()))
    if not max_:
        if sum(lst_temp):
            max_ = 1
    grd_.append(lst_temp)

grd_dp = [[[grd_[idx_r][idx_c], grd_[idx_r][idx_c]] for idx_c in range(C_)] for idx_r in range(R_)]

lst_ = []
for idx_r in range(1, R_):
    for idx_c in range(C_):
        if grd_[idx_r][idx_c]:
            if 0 < idx_c:
                grd_dp[idx_r][idx_c][0] += grd_dp[idx_r - 1][idx_c - 1][0]
            if idx_c < C_ - 1:
                grd_dp[idx_r][idx_c][1] += grd_dp[idx_r - 1][idx_c + 1][1]
            min_ = min(grd_dp[idx_r][idx_c])
            if min_ > 1:
                lst_.append((min_, idx_r, idx_c))

for min_, idx_r, idx_c in sorted(lst_, reverse=True):
    print(min_, idx_r, idx_c)
    if min_ <= max_:
        break
    for offset_ in range(min_, max_, -1):
        if (idx_c + offset_ - 1) < C_ and (idx_c - offset_ + 1) >= 0 and idx_r - offset_ + 1 >= 0 and \
                grd_dp[idx_r - offset_ + 1][idx_c + offset_ - 1][0] >= offset_ and \
                grd_dp[idx_r - offset_ + 1][idx_c - offset_ + 1][1] >= offset_:
            max_ = max(max_, offset_)

print(max_)

exit()
