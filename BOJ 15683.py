import sys
import copy

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
grd_c = [[True for _ in range(C_)] for _ in range(R_)]
lst_ = []
lst_5 = []
rem_ = R_ * C_
for idx_r in range(R_):
    lst_temp = list(map(int, sys.stdin.readline().split()))
    for idx_c, value_ in enumerate(lst_temp):
        if 1 <= value_ <= 4:
            lst_.append((idx_r, idx_c, value_))
            grd_c[idx_r][idx_c] = False
            rem_ -= 1
        elif value_ == 5:
            lst_5.append((idx_r, idx_c))
            grd_c[idx_r][idx_c] = False
            rem_ -= 1
        elif value_ == 6:
            rem_ -= 1
    grd_.append(lst_temp)

for each_ in grd_c:
    print(each_)
print(rem_)

for idx_r, idx_c in lst_5:
    temp_r = idx_r + 1
    while temp_r < R_:
        if grd_[temp_r][idx_c] != 6:
            if grd_c[temp_r][idx_c]:
                grd_c[temp_r][idx_c] = False
                rem_ -= 1
        else:
            break
        temp_r += 1

    temp_r = idx_r - 1
    while temp_r >= 0:
        if grd_[temp_r][idx_c] != 6:
            if grd_c[temp_r][idx_c]:
                grd_c[temp_r][idx_c] = False
                rem_ -= 1
        else:
            break
        temp_r -= 1

    temp_c = idx_c + 1
    while temp_c < C_:
        if grd_[idx_r][temp_c] != 6:
            if grd_c[idx_r][temp_c]:
                grd_c[idx_r][temp_c] = False
                rem_ -= 1
        else:
            break
        temp_c += 1

    temp_c = idx_c - 1
    while temp_c >= 0:
        if grd_[idx_r][temp_c] != 6:
            if grd_c[idx_r][temp_c]:
                grd_c[idx_r][temp_c] = False
                rem_ -= 1
        else:
            break
        temp_c -= 1

lst_type = [[], [0], [0, 2], [0, 1], [0, 1, 2]]

min_ = rem_
for cnt_ in range(4 ** len(lst_)):
    grd_c_temp = copy.deepcopy(grd_c)
    rem_temp = rem_

    lst_com = []
    for _ in range(len(lst_) - 1):
        cnt_, com_ = divmod(cnt_, 4)
        lst_com.append(com_)
    lst_com.append(cnt_)

    for (idx_r, idx_c, type_), com_ in zip(lst_, lst_com):
        set_type = set([(val_ + com_) % 4 for val_ in lst_type[type_]])
        if 0 in set_type:
            temp_r = idx_r + 1
            while temp_r < R_:
                if grd_[temp_r][idx_c] != 6:
                    if grd_c_temp[temp_r][idx_c]:
                        grd_c_temp[temp_r][idx_c] = False
                        rem_temp -= 1
                else:
                    break
                temp_r += 1

        if 2 in set_type:
            temp_r = idx_r - 1
            while temp_r >= 0:
                if grd_[temp_r][idx_c] != 6:
                    if grd_c_temp[temp_r][idx_c]:
                        grd_c_temp[temp_r][idx_c] = False
                        rem_temp -= 1
                else:
                    break
                temp_r -= 1

        if 1 in set_type:
            temp_c = idx_c + 1
            while temp_c < C_:
                if grd_[idx_r][temp_c] != 6:
                    if grd_c_temp[idx_r][temp_c]:
                        grd_c_temp[idx_r][temp_c] = False
                        rem_temp -= 1
                else:
                    break
                temp_c += 1

        if 3 in set_type:
            temp_c = idx_c - 1
            while temp_c >= 0:
                if grd_[idx_r][temp_c] != 6:
                    if grd_c_temp[idx_r][temp_c]:
                        grd_c_temp[idx_r][temp_c] = False
                        rem_temp -= 1
                else:
                    break
                temp_c -= 1
    min_ = min(min_, rem_temp)

print(min_)

exit()
