import sys
from itertools import combinations as cb

dct_cb = dict()


def comb_(N_, C_):
    if (N_, C_) not in dct_cb:
        ret_ = 1
        for a_, b_ in zip(range(N_, N_ - C_ - 1, -1), range(1, C_ + 1)):
            ret_ *= a_
            ret_ //= b_
        dct_cb[(N_, C_)] = ret_
    return dct_cb[(N_, C_)]


N_ = int(sys.stdin.readline())

if N_ < 4:
    print(0)
else:
    tot_ = 13


    print(tot_)
exit()
