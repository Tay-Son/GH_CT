import sys
import math

N, M, K = map(int, sys.stdin.readline().split())
lst_ = []

tre_ = [0 for _ in range(pow(2, math.ceil(math.log2(N)) + 1))]


def edt_(idx_, diff_):
    ptr_tre = 1
    idx_l = 0
    idx_r = N - 1
    while idx_l < idx_r:
        tre_[ptr_tre] += diff_
        idx_t = (idx_l + idx_r) // 2
        if idx_ <= idx_t:
            idx_r = idx_t
            ptr_tre *= 2
        else:
            idx_l = idx_t + 1
            ptr_tre *= 2
            ptr_tre += 1
    tre_[ptr_tre] += diff_


def sum_(s_, e_, idx_l, idx_r, ptr_tre):
    if idx_r < s_ or e_ < idx_l:
        return 0
    elif s_ <= idx_l and idx_r <= e_:
        return tre_[ptr_tre]
    else:
        return sum_(s_, e_, idx_l, (idx_l + idx_r) // 2, ptr_tre * 2) + \
               sum_(s_, e_, (idx_l + idx_r) // 2 + 1, idx_r, ptr_tre * 2 + 1)


for cnt_ in range(N):
    input_ = int(sys.stdin.readline())
    lst_.append(input_)

    edt_(cnt_, input_)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        diff_ = c - lst_[b]
        lst_[b] = c
        edt_(b, diff_)
    else:
        b -= 1
        c -= 1
        print(sum_(b, c, 0, N - 1, 1))
