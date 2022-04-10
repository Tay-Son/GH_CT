import sys

sys.setrecursionlimit(10 ** 6)

lst_l = [0 for _ in range(10001)]
lst_r = [0 for _ in range(10001)]
lst_x = [0 for _ in range(10001)]
lst_p = [-1 for _ in range(10001)]

N_ = 0
R_ = 0
cnt_ = 0


def rec_(idx_, lim_):
    global cnt_

    l_ = rec_(lst_l[idx_], lim_) if lst_l[idx_] != -1 else 0
    r_ = rec_(lst_r[idx_], lim_) if lst_r[idx_] != -1 else 0

    if lst_x[idx_] + l_ + r_ <= lim_:
        return lst_x[idx_] + l_ + r_
    else:
        if lst_x[idx_] + min(l_, r_) <= lim_:
            cnt_ += 1
            return lst_x[idx_] + min(l_, r_)
        else:
            cnt_ += 2
            return lst_x[idx_]


def solution(K_, lst_N, tre_):
    global R_, cnt_
    for idx_ in range(len(lst_N)):
        lst_l[idx_], lst_r[idx_] = tre_[idx_]
        lst_x[idx_] = lst_N[idx_]
        if lst_l[idx_] != -1:
            idx_temp = lst_l[idx_]
            lst_p[idx_temp] = idx_
        if lst_r[idx_] != -1:
            idx_temp = lst_r[idx_]
            lst_p[idx_temp] = idx_

    for idx_ in range(len(lst_N)):
        if lst_p[idx_] == -1:
            R_ = idx_
            break

    ptr_s = max(lst_x)
    ptr_e = 10 ** 8
    while ptr_s < ptr_e:
        ptr_c = (ptr_s + ptr_e) // 2
        cnt_ = 0
        rec_(R_, ptr_c)
        cnt_ += 1
        if cnt_ <= K_:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1

    return ptr_s
