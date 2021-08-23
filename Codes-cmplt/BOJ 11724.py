import sys

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(M_):
    A_, B_ = map(int, sys.stdin.readline().split())
    grp_[A_].append(B_)
    grp_[B_].append(A_)

lst_is = [False for _ in range(N_ + 1)]


def func(idx_):
    if lst_is[idx_] == False:
        lst_is[idx_] = True
        for each_ in grp_[idx_]:
            func(each_)
        return 1
    else:
        return 0


cnt_ = 0
for idx_ in range(1, N_ + 1):
    cnt_ += func(idx_)
print(cnt_)
