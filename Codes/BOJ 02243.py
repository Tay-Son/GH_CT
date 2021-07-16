import sys

FLA_MAX = 20
tre_ = [0 for _ in range(2 ** (FLA_MAX + 1))]


def set_(idx_, val_):
    idx_curr = 1
    ptr_div = 2 ** (FLA_MAX - 1)
    ptr_tre = ptr_div
    tre_[idx_curr] += val_
    for _ in range(FLA_MAX):
        ptr_div //= 2
        idx_curr *= 2
        if idx_ >= ptr_tre:
            idx_curr += 1
            ptr_tre += ptr_div
        else:

            ptr_tre -= ptr_div
        tre_[idx_curr] += val_


def take_(rank_):
    idx_target = 0

    ptr_div = 2 ** (FLA_MAX - 1)
    ptr_curr = 1
    ptr_tre = 0

    for _ in range(FLA_MAX):
        ptr_curr *= 2
        if rank_ <= ptr_tre + tre_[ptr_curr]:
            pass
        else:
            ptr_tre += tre_[ptr_curr]
            ptr_curr += 1
            idx_target += ptr_div
        ptr_div //= 2
    set_(idx_target, -1)
    return idx_target


lst_ = [0 for _ in range(FLA_MAX + 1)]

for _ in range(int(sys.stdin.readline())):
    lst_input = list(map(int, sys.stdin.readline().split()))
    if lst_input[0] == 1:
        print(take_(lst_input[1]))
    else:
        set_(lst_input[1], lst_input[2])
exit()