import sys
import math

INF_ = sys.maxsize
N_, M_ = map(int, sys.stdin.readline().split())
tre_ = [[INF_, 0] for _ in range(2 ** (math.ceil(math.log2(N_ + 1)) + 1))]


def set(idx_, val_):
    idx_t = 1
    ptr_s = 0
    ptr_e = N_

    while ptr_s != ptr_e:
        tre_[idx_t][0] = min(tre_[idx_t][0], val_)
        tre_[idx_t][1] = max(tre_[idx_t][1], val_)
        idx_t *= 2

        ptr_c = (ptr_s + ptr_e) // 2
        if idx_ <= ptr_c:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1
            idx_t += 1

    tre_[idx_t][0] = min(tre_[idx_t][0], val_)
    tre_[idx_t][1] = max(tre_[idx_t][1], val_)


def acc(idx_s, idx_e, idx_t, ptr_s, ptr_e):
    if idx_s == ptr_s and idx_e == ptr_e:
        return tre_[idx_t]
    else:
        ret_ = [INF_, 0]
        ptr_c = (ptr_s + ptr_e) // 2
        if idx_s <= ptr_c:
            temp_ = acc(idx_s, min(idx_e, ptr_c), idx_t * 2, ptr_s, ptr_c)
            ret_[0] = min(ret_[0], temp_[0])
            ret_[1] = max(ret_[1], temp_[1])
        if ptr_c < idx_e:
            temp_ = acc(max(idx_s, ptr_c + 1), idx_e, idx_t * 2 + 1, ptr_c + 1, ptr_e)
            ret_[0] = min(ret_[0], temp_[0])
            ret_[1] = max(ret_[1], temp_[1])
        return ret_


for idx_ in range(1, N_ + 1):
    set(idx_, int(sys.stdin.readline()))

for _ in range(M_):
    a_, b_ = map(int, sys.stdin.readline().split())
    print(' '.join(map(str, acc(a_, b_, 1, 0, N_))))

exit()
