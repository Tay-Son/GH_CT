import sys
import math

INF_ = 1000000007

N_ = int(sys.stdin.readline())

cch_ = 2 ** math.ceil(math.log2(N_ + 1))

tre_ = [0 for _ in range(cch_ * 2)]


def update_(idx_, value_):
    # print(idx_, value_)
    lst_[idx_] = value_
    idx_tre = idx_ + cch_
    tre_[idx_tre] = idx_
    idx_tre //= 2
    while idx_tre:
        # print(tre_)
        # print(idx_, tre_[idx_ * 2], tre_[idx_ * 2 + 1])
        if lst_[tre_[idx_tre * 2]] <= lst_[tre_[idx_tre * 2 + 1]]:
            tre_[idx_tre] = tre_[idx_tre * 2]
        else:
            tre_[idx_tre] = tre_[idx_tre * 2 + 1]
        idx_tre //= 2


def get_(idx_tre, idx_s, idx_e, ptr_l, ptr_r):
    # print(idx_tre, idx_s, idx_e, ptr_l, ptr_r)
    if idx_s == ptr_l and idx_e == ptr_r:
        return tre_[idx_tre]
    else:
        ptr_c = (ptr_l + ptr_r) // 2
        min_idx = 0
        if idx_s < ptr_c:
            temp_ = get_(idx_tre * 2, idx_s, min(idx_e, ptr_c), ptr_l, ptr_c)
            if lst_[min_idx] > lst_[temp_]:
                min_idx = temp_

        if ptr_c < idx_e:
            temp_ = get_(idx_tre * 2 + 1, max(ptr_c, idx_s), idx_e, ptr_c, ptr_r)
            if lst_[min_idx] > lst_[temp_]:
                min_idx = temp_
        return min_idx


print(len(tre_))
print(tre_)
lst_ = [INF_ for _ in range(cch_)]
print(lst_)

for idx_, value_ in enumerate(map(int, sys.stdin.readline().split())):
    idx_ += 1
    update_(idx_, value_)
print(lst_)
print(tre_)

for _ in range(int(sys.stdin.readline())):
    com_, val_a, val_b = map(int, sys.stdin.readline().split())
    if com_ == 1:
        update_(val_a, val_b)
    elif com_ == 2:
        print(get_(1, val_a, val_b + 1, 0, cch_))

exit()
