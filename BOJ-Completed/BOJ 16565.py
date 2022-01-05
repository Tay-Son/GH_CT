import sys

DIV_ = 10007

dct_comb = {}


def comb_(val_a, val_b):
    val_b = min(val_b, val_a - val_b)
    if (val_a, val_b) not in dct_comb:
        if not val_b:
            dct_comb[(val_a, val_b)] = 1
        else:
            dct_comb[val_a, val_b] = comb_(val_a - 1, val_b - 1) + comb_(val_a - 1, val_b)
    return dct_comb[val_a, val_b]


N_ = int(sys.stdin.readline())
tot_ = 0
for num_ in range(4, N_ + 1, 4):
    if (num_ // 4) % 2:
        tot_ += comb_(13, num_ // 4) * comb_(52 - num_, N_ - num_)
    else:
        tot_ -= comb_(13, num_ // 4) * comb_(52 - num_, N_ - num_)
    tot_ %= DIV_

print(tot_)
exit()
