import sys
import math

N_ = int(sys.stdin.readline())
tre_depth = math.ceil(math.log2(N_ + 1))
cch_tpd = 2 ** tre_depth
tre_ = [0 for _ in range(2 ** tre_depth)]
tre_ += [idx_ for idx_ in range(2 ** tre_depth)]

lst_ = [10 ** 9] + list(map(int, sys.stdin.readline().split()))
lst_ += [10 ** 9 for _ in range(2 ** tre_depth - 1 - N_)]

for idx_tre in range(2 ** tre_depth - 1, -1, -1):
    temp_ = lst_[tre_[idx_tre*2]]-lst_[tre_[idx_tre * 2 + 1]]
    if temp_ <= 0:
        tre_[idx_tre] = tre_[idx_tre*2]
    else:
        tre_[idx_tre] = tre_[idx_tre * 2 + 1]

def set_(idx_, val_new):
    lst_[idx_] = val_new
    idx_tre = (cch_tpd + idx_) // 2

    while idx_tre > 0:
        temp_ = lst_[tre_[idx_tre * 2]] - lst_[tre_[idx_tre * 2 + 1]]
        if temp_ <= 0:
            tre_[idx_tre] = tre_[idx_tre * 2]
        else:
            tre_[idx_tre] = tre_[idx_tre * 2 + 1]
        idx_tre //= 2

for _ in range(int(sys.stdin.readline())):
    lst_input = list(map(int, sys.stdin.readline().split()))
    if lst_input[0] == 1:
        set_(lst_input[1], lst_input[2])
    else:
        print(tre_[1])

exit()