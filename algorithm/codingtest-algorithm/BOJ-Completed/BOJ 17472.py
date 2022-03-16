import sys


def find_(lst_p, idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(lst_p, temp_)
        lst_p[idx_] = temp_
    return temp_


def union_(lst_p, idx_a, idx_b):
    p_a, p_b = find_(lst_p, idx_a), find_(lst_p, idx_b)
    if p_a < p_b:
        lst_p[p_b] = p_a
    else:
        lst_p[p_a] = p_b


N_, M_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(lambda x: int(x) - 1, sys.stdin.readline().split())))

lst_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs_(idx_n, idx_m, cnt_):
    grd_[idx_n][idx_m] = cnt_
    for offset_n, offset_m in lst_offset:
        idx_target_n = idx_n + offset_n
        idx_target_m = idx_m + offset_m
        if 0 <= idx_target_n < N_ and 0 <= idx_target_m < M_ and not grd_[idx_target_n][idx_target_m]:
            bfs_(idx_target_n, idx_target_m, cnt_)


cnt_ = 1
for idx_n in range(N_):
    for idx_m in range(M_):
        if not grd_[idx_n][idx_m]:
            bfs_(idx_n, idx_m, cnt_)
            cnt_ += 1
lst_p = [idx_ for idx_ in range(cnt_)]

lst_ = []
for idx_n in range(N_):
    idx_s = 0
    cnt_ = 0
    for idx_m in range(M_):
        temp_ = grd_[idx_n][idx_m]
        if temp_ > 0:
            if idx_m > 1 and grd_[idx_n][idx_m - 1] < 0 and cnt_ >= 2 and idx_s > 0 and idx_s != temp_:
                lst_.append((cnt_, idx_s, temp_))
            idx_s = temp_
            cnt_ = 0
        else:
            cnt_ += 1

for idx_m in range(M_):
    idx_s = 0
    cnt_ = 0
    for idx_n in range(N_):
        temp_ = grd_[idx_n][idx_m]
        if temp_ > 0:
            if idx_n > 1 and grd_[idx_n - 1][idx_m] < 0 and cnt_ >= 2 and idx_s > 0 and idx_s != temp_:
                lst_.append((cnt_, idx_s, temp_))
            idx_s = temp_
            cnt_ = 0
        else:
            cnt_ += 1

lst_.sort()

cnt_ = 1
tot_ = 0
idx_lst = 0

while idx_lst < len(lst_) and cnt_ < len(lst_p):
    weight_, idx_a, idx_b = lst_[idx_lst]
    if find_(lst_p, idx_a) != find_(lst_p, idx_b):
        print(weight_, idx_a, idx_b)
        union_(lst_p, idx_a, idx_b)
        cnt_ += 1
        tot_ += weight_
    idx_lst += 1

print()
for each_ in lst_:
    print(each_)
print()

for each_ in grd_:
    print(list(map(lambda x: 0 if x == -1 else x, each_)))
print()


if cnt_ == len(lst_p) - 1:
    print(tot_)
else:
    print(-1)

exit()
