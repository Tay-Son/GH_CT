import sys

N_ = int(sys.stdin.readline())
lst_p = list(map(int, sys.stdin.readline().split()))

tre_ = [[] for _ in range(N_)]
for idx_, idx_p in enumerate(lst_p):
    if idx_p == -1:
        root_ = idx_
    else:
        tre_[idx_p].append(idx_)
D_ = int(sys.stdin.readline())


def rec_(idx_):
    if idx_ == D_:
        return 0
    else:
        if not len(tre_[idx_]):
            return 1
        else:
            tot_ = 0
            for idx_c in tre_[idx_]:
                tot_ += rec_(idx_c)
            return max(1, tot_)


print(rec_(root_))

exit()
