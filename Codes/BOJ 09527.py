import sys

dct_ = {}
dct_[0] = 0


def func(idx_):
    if idx_ not in dct_:
        c_ = 2 ** (len(str(bin(idx_))) - 3)
        dct_[idx_] = int(func(c_ - 1) + func(idx_ - c_) + idx_ - c_ + 1)

    return dct_[idx_]


A, B = map(int, sys.stdin.readline().split())
print(func(B) - func(A - 1))

exit()