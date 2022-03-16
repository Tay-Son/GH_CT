import sys

N_, P_, Q_ = map(int, sys.stdin.readline().split())
dct_ = {0: 1}


def rec_(idx_):
    if idx_ not in dct_:
        dct_[idx_] = rec_(idx_ // P_) + rec_(idx_ // Q_)
    return dct_[idx_]

print(rec_(N_))

exit()