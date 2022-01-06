import sys
import math

N_, M_ = map(int, sys.stdin.readline().split())
lst_orig = [0 for _ in range(N_ + 1)]
tre_ = [0 for _ in range(2 ** math.ceil(math.log2(N_ + 1) + 1))]


def mod(idx_, val_):
    orig_ = lst_orig[idx_]
    lst_orig[idx_] = val_
    idx_tre = 1

    ptr_s = 0
    ptr_e = N_
    while ptr_s != ptr_e:
        tre_[idx_tre] -= orig_
        tre_[idx_tre] += val_

        idx_tre *= 2
        ptr_c = (ptr_s + ptr_e) // 2
        if idx_ <= ptr_c:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1
            idx_tre += 1
    tre_[idx_tre] = val_


def acc(idx_s, idx_e, idx_tre, ptr_s, ptr_e):
    if idx_s == ptr_s and idx_e == ptr_e:
        return tre_[idx_tre]
    else:
        ptr_c = (ptr_s + ptr_e) // 2
        ret_ = 0
        if idx_s <= ptr_c:
            ret_ += acc(idx_s, min(idx_e, ptr_c), idx_tre * 2, ptr_s, ptr_c)
        if ptr_c < idx_e:
            ret_ += acc(max(idx_s, ptr_c + 1), idx_e, idx_tre * 2 + 1, ptr_c + 1, ptr_e)
        return ret_


cnt_ = 1
for each_ in map(int, sys.stdin.readline().split()):
    mod(cnt_, each_)
    cnt_ += 1

for _ in range(M_):
    A_, B_, C_, D_ = map(int, sys.stdin.readline().split())
    print(acc(min(A_, B_), max(A_, B_), 1, 0, N_))
    mod(C_, D_)

exit()
