import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_.sort()
min_ = 1000000000 * 3
lst_min = []
for ptr_a in range(N_ - 2):
    val_a = lst_[ptr_a]
    ptr_l = ptr_a + 1
    ptr_r = N_ - 1
    while ptr_l < ptr_r:
        val_l = lst_[ptr_l]
        val_r = lst_[ptr_r]
        val_t = val_a + val_l + val_r
        val_abs = abs(val_t)
        if val_abs < min_:
            min_ = val_abs
            lst_min = [val_a, val_l, val_r]
        if val_t < 0:
            ptr_l += 1
        else:
            ptr_r -= 1

print(' '.join(map(str, lst_min)))

exit()
