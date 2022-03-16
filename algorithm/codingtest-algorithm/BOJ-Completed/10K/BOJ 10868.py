import sys
import math

N_, M_ = map(int, sys.stdin.readline().split())
INF_ = sys.maxsize
tre_ = [INF_ for _ in range(2 ** (math.ceil(math.log2(N_ + 1)) + 1))]


def set(idx_, val):
    idx_t = 1
    ptr_s = 0
    ptr_e = N_

    while ptr_s != ptr_e:
        tre_[idx_t] = min(tre_[idx_t], val)
        idx_t *= 2
        ptr_c = (ptr_s + ptr_e) // 2
        if idx_ <= ptr_c:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1
            idx_t += 1
    tre_[idx_t] = min(tre_[idx_t], val)


def acc(idx_s, idx_e, idx_t, ptr_s, ptr_e):
    if idx_s == ptr_s and idx_e == ptr_e:
        return tre_[idx_t]
    else:
        ret_ = INF_
        ptr_c = (ptr_s + ptr_e) // 2
        if idx_s <= ptr_c:
            ret_ = min(ret_, acc(idx_s, min(idx_e, ptr_c), idx_t * 2, ptr_s, ptr_c))
        if ptr_c < idx_e:
            ret_ = min(ret_, acc(max(idx_s, ptr_c + 1), idx_e, idx_t * 2 + 1, ptr_c + 1, ptr_e))
        return ret_


for idx_ in range(1, N_ + 1):
    set(idx_, int(sys.stdin.readline()))

for _ in range(M_):
    idx_s, idx_e = map(int, sys.stdin.readline().split())
    print(acc(idx_s, idx_e, 1, 0, N_))

exit()
