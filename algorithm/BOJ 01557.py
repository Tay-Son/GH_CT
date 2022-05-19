import sys

lst_mu = [0 for _ in range(1000001)]
lst_mu[1] = 1
for idx_ in range(1, 1000001):
    for idx_sub in range(idx_ * 2, 1000001, idx_):
        lst_mu[idx_sub] -= lst_mu[idx_]


def c_(num_):
    tot_ = 0
    for idx_ in range(1, int(num_ ** .5) + 1):
        tot_ += lst_mu[idx_] * (num_ // (idx_ * idx_))
    return tot_


K_ = int(sys.stdin.readline())
ptr_l = 0
ptr_r = 2 * K_
while ptr_l < ptr_r - 1:
    ptr_c = (ptr_l + ptr_r) // 2
    temp_ = c_(ptr_c)

    print(ptr_l, ptr_r, ptr_c, temp_, K_)
    if temp_ < K_:
        ptr_l = ptr_c
    else:
        ptr_r = ptr_c

print(ptr_r)

exit()
