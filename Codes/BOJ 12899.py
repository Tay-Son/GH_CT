import sys
import math

C_ = 21
N_ = 2 ** C_
lst_is = [False for _ in range(N_)]
tre_ = [0 for _ in range(N_)]


def on(idx_):
    lst_is[idx_] = True
    idx_tre = 1
    for cnt_ in range(C_ - 1, -1, -1):
        temp_ = 2 ** cnt_
        if idx_ <= temp_:
            tre_[idx_tre] += 1
            idx_tre *= 2
        else:
            idx_ -= temp_
            idx_tre *= 2
            idx_tre += 1


def query(cnt_):
    cnt_ -= 1
    idx_tre = 1
    idx_ = 0
    for x_ in range(C_ - 1, -1, -1):
        temp_ = tre_[idx_tre]
        if cnt_ < temp_:
            tre_[idx_tre] -= 1
            idx_tre *= 2
        else:
            cnt_ -= temp_
            idx_ += 2 ** x_
            idx_tre *= 2
            idx_tre += 1
    lst_is[idx_ - 1] = False
    return idx_ + 1


for _ in range(int(sys.stdin.readline())):
    T_, X_ = map(int, sys.stdin.readline().split())
    if T_ == 1:
        on(X_)
    else:
        print(query(X_))

exit()
