import sys

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
tot_ = 0

grd_intp = []
for a_ in 'IE':
    for b_ in 'NS':
        for c_ in 'FT':
            for d_ in 'PJ':
                grd_intp.append([a_, b_, c_, d_])
                grd_intp.append([d_, c_, b_, a_])


def cnt_(lst_):
    tot_ = 0
    for idx_s in range(len(lst_) - 3):
        for intp_ in grd_intp:
            if lst_[idx_s:idx_s + 4] == intp_:
                tot_ += 1
    return tot_


for _ in range(R_):
    lst_temp = list(sys.stdin.readline().rstrip())
    tot_ += cnt_(lst_temp)
    grd_.append(lst_temp)
    print(lst_temp, tot_)
print()

for idx_c in range(C_):
    lst_temp = []
    for idx_r in range(R_):
        lst_temp.append(grd_[idx_r][idx_c])
    tot_ += cnt_(lst_temp)
    print(lst_temp, tot_)
print()

for num_ in range(-R_, C_ - 1):
    idx_r, idx_c = max(-num_ - 1, 0), max(num_ + 1, 0)
    # print(idx_r, idx_c)
    lst_temp = []
    while idx_r < R_ and idx_c < C_:
        lst_temp.append(grd_[idx_r][idx_c])
        idx_r += 1
        idx_c += 1
    tot_ += cnt_(lst_temp)
    print(lst_temp, tot_)
print()

for num_ in range(R_ + C_ - 1):
    idx_r, idx_c = max(num_ - C_ + 1, 0), min(num_, C_ - 1)
    # print(idx_r, idx_c)
    lst_temp = []
    while idx_r < R_ and 0 <= idx_c:
        lst_temp.append(grd_[idx_r][idx_c])
        idx_r += 1
        idx_c -= 1
    tot_ += cnt_(lst_temp)
    print(lst_temp, tot_)

print(tot_)

exit()
