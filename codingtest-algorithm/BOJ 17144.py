import sys

R_, C_, T_ = map(int, sys.stdin.readline().split())

grd_ = []
lst_h = []
tot_ = 0
for idx_r in range(R_):
    lst_temp = []
    for idx_c, value_ in enumerate(map(int, sys.stdin.readline().split())):
        if value_ >= 0:
            tot_ += value_
        else:
            lst_h.append(idx_r)
        lst_temp.append(value_)
    grd_.append(lst_temp)

for each_ in grd_:
    print(each_)
print()

for _ in range(T_):
    grd_temp = [[0 for _ in range(C_)] for _ in range(R_)]
    for idx_r in range(R_):
        for idx_c in range(C_):
            if grd_[idx_r][idx_c] > 0:
                v_c = grd_[idx_r][idx_c]
                v_f = v_c // 5
                for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    t_r, t_c = idx_r + o_r, idx_c + o_c
                    if 0 <= t_r < R_ and 0 <= t_c < C_ and grd_[t_r][t_c] != -1:
                        v_c -= v_f
                        grd_temp[t_r][t_c] += v_f
                grd_temp[idx_r][idx_c] += v_c

    tot_ -= grd_temp[lst_h[0] - 1][0]
    tot_ -= grd_temp[lst_h[1] + 1][0]

    for each_ in grd_temp:
        print(each_)
    print()

    for idx_r in range(lst_h[0] - 2, -1, -1):
        grd_temp[idx_r + 1][0] = grd_temp[idx_r][0]
    for idx_r in range(lst_h[1] + 2, R_):
        grd_temp[idx_r - 1][0] = grd_temp[idx_r][0]

    grd_temp[0].pop(0)
    grd_temp[0].append(0)
    grd_temp[R_ - 1].pop(0)
    grd_temp[R_ - 1].append(0)

    for idx_r in range(1, lst_h[0] + 1):
        grd_temp[idx_r - 1][C_ - 1] = grd_temp[idx_r][C_ - 1]
    for idx_r in range(R_ - 2, lst_h[1] - 1, -1):
        grd_temp[idx_r + 1][C_ - 1] = grd_temp[idx_r][C_ - 1]

    grd_temp[lst_h[0]].pop(-1)
    grd_temp[lst_h[0]].insert(0, 0)
    grd_temp[lst_h[1]].pop(-1)
    grd_temp[lst_h[1]].insert(0, 0)

    grd_temp[lst_h[0]][0] = -1
    grd_temp[lst_h[1]][0] = -1
    grd_ = grd_temp

    for each_ in grd_:
        print(each_)
    print()

print(tot_)

exit()
